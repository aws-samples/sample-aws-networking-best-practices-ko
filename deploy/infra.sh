#!/usr/bin/env bash
# S3(비공개) + CloudFront(OAC) 정적 호스팅 인프라를 생성한다.
#
# 보안/기능 요점:
#   - S3: 퍼블릭 액세스 전면 차단 + 기본 암호화(SSE-S3) + REST 오리진(웹사이트 엔드포인트 미사용)
#   - CloudFront: OAC(SigV4)로만 S3 읽기, 뷰어는 HTTPS 강제(redirect-to-https)
#   - 버킷 정책: 해당 배포(SourceArn)에서 온 요청만 허용
#   - 보안 응답 헤더: AWS 관리형 SecurityHeadersPolicy(HSTS·nosniff·frame·referrer)
#   - 디렉토리 인덱스: CloudFront Function(viewer-request)으로 /path/ -> /path/index.html
#
# 사용: bash deploy/infra.sh <bucket-name> [region]
set -euo pipefail

BUCKET="${1:?사용법: infra.sh <bucket-name> [region]}"
REGION="${2:-us-east-1}"
COMMENT="aws-networking-best-practices-ko"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# AWS 관리형 정책 ID(전 리전 공통, 고정값)
CACHE_POLICY_OPTIMIZED="658327ea-f89d-4fab-a63d-7e88639e58f6"      # CachingOptimized
RESPONSE_HEADERS_SECURITY="67f7725c-6f97-4210-82d7-5512b31e9d03"   # SecurityHeadersPolicy

echo "▶ S3 버킷 생성: $BUCKET ($REGION)"
if [ "$REGION" = "us-east-1" ]; then
  aws s3api create-bucket --bucket "$BUCKET" --region "$REGION" 2>/dev/null || true
else
  aws s3api create-bucket --bucket "$BUCKET" --region "$REGION" \
    --create-bucket-configuration LocationConstraint="$REGION" 2>/dev/null || true
fi

echo "▶ S3 퍼블릭 액세스 전면 차단"
aws s3api put-public-access-block --bucket "$BUCKET" \
  --public-access-block-configuration \
  BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true

echo "▶ S3 기본 암호화(SSE-S3) + 버킷 키"
aws s3api put-bucket-encryption --bucket "$BUCKET" \
  --server-side-encryption-configuration '{
    "Rules": [{
      "ApplyServerSideEncryptionByDefault": { "SSEAlgorithm": "AES256" },
      "BucketKeyEnabled": true
    }]
  }'

echo "▶ CloudFront Function 생성/게시 (디렉토리 인덱스 재작성)"
FN_NAME="${BUCKET}-rewrite"
FN_ARN=$(aws cloudfront create-function \
  --name "$FN_NAME" \
  --function-config "Comment=dir-index rewrite for ${COMMENT},Runtime=cloudfront-js-2.0" \
  --function-code "fileb://${SCRIPT_DIR}/cf-function.js" \
  --query 'FunctionSummary.FunctionMetadata.FunctionARN' --output text 2>/dev/null || \
  aws cloudfront describe-function --name "$FN_NAME" \
  --query 'FunctionSummary.FunctionMetadata.FunctionARN' --output text)
# 게시(DEVELOPMENT -> LIVE). 이미 최신이면 ETag 갱신 후 재게시.
FN_ETAG=$(aws cloudfront describe-function --name "$FN_NAME" --query 'ETag' --output text)
aws cloudfront publish-function --name "$FN_NAME" --if-match "$FN_ETAG" >/dev/null
echo "  FunctionARN: $FN_ARN"

echo "▶ CloudFront Origin Access Control 생성"
OAC_ID=$(aws cloudfront create-origin-access-control \
  --origin-access-control-config \
  "Name=${BUCKET}-oac,SigningProtocol=sigv4,SigningBehavior=always,OriginAccessControlOriginType=s3" \
  --query 'OriginAccessControl.Id' --output text 2>/dev/null || \
  aws cloudfront list-origin-access-controls \
  --query "OriginAccessControlList.Items[?Name=='${BUCKET}-oac'].Id" --output text)

echo "▶ CloudFront 배포 생성 (HTTPS 강제 + 보안 헤더 + 디렉토리 재작성)"
DIST_CONFIG=$(cat <<JSON
{
  "CallerReference": "${BUCKET}-$(date +%s)",
  "Comment": "${COMMENT}",
  "Enabled": true,
  "DefaultRootObject": "index.html",
  "HttpVersion": "http2and3",
  "Origins": {
    "Quantity": 1,
    "Items": [{
      "Id": "s3-${BUCKET}",
      "DomainName": "${BUCKET}.s3.${REGION}.amazonaws.com",
      "OriginAccessControlId": "${OAC_ID}",
      "S3OriginConfig": { "OriginAccessIdentity": "" }
    }]
  },
  "DefaultCacheBehavior": {
    "TargetOriginId": "s3-${BUCKET}",
    "ViewerProtocolPolicy": "redirect-to-https",
    "CachePolicyId": "${CACHE_POLICY_OPTIMIZED}",
    "ResponseHeadersPolicyId": "${RESPONSE_HEADERS_SECURITY}",
    "Compress": true,
    "FunctionAssociations": {
      "Quantity": 1,
      "Items": [{ "EventType": "viewer-request", "FunctionARN": "${FN_ARN}" }]
    }
  },
  "CustomErrorResponses": {
    "Quantity": 2,
    "Items": [
      { "ErrorCode": 404, "ResponsePagePath": "/404.html", "ResponseCode": "404", "ErrorCachingMinTTL": 60 },
      { "ErrorCode": 403, "ResponsePagePath": "/404.html", "ResponseCode": "404", "ErrorCachingMinTTL": 60 }
    ]
  }
}
JSON
)
DIST_JSON=$(aws cloudfront create-distribution --distribution-config "$DIST_CONFIG")
DIST_ID=$(echo "$DIST_JSON" | python3 -c "import sys,json;print(json.load(sys.stdin)['Distribution']['Id'])")
DOMAIN=$(echo "$DIST_JSON" | python3 -c "import sys,json;print(json.load(sys.stdin)['Distribution']['DomainName'])")

echo "▶ S3 버킷 정책: CloudFront(OAC)만 읽기 허용"
ACCOUNT=$(aws sts get-caller-identity --query Account --output text)
aws s3api put-bucket-policy --bucket "$BUCKET" --policy "$(cat <<JSON
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowCloudFrontOAC",
      "Effect": "Allow",
      "Principal": { "Service": "cloudfront.amazonaws.com" },
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::${BUCKET}/*",
      "Condition": { "StringEquals": { "AWS:SourceArn": "arn:aws:cloudfront::${ACCOUNT}:distribution/${DIST_ID}" } }
    },
    {
      "Sid": "DenyInsecureTransport",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:*",
      "Resource": [
        "arn:aws:s3:::${BUCKET}",
        "arn:aws:s3:::${BUCKET}/*"
      ],
      "Condition": { "Bool": { "aws:SecureTransport": "false" } }
    }
  ]
}
JSON
)"

cat <<EOF

✅ 완료
  S3 버킷                : ${BUCKET}  (비공개 · SSE-S3)
  CloudFront 배포 ID     : ${DIST_ID}
  CloudFront 도메인      : https://${DOMAIN}
  보안 헤더 정책         : SecurityHeadersPolicy (HSTS 포함)
  URL 재작성 함수        : ${FN_NAME} (LIVE)

다음 단계:
  1) 사이트 업로드:  aws s3 sync site "s3://${BUCKET}" --delete
  2) 캐시 무효화:    aws cloudfront create-invalidation --distribution-id ${DIST_ID} --paths "/*"

GitHub repo 변수(자동 배포 시):
  DEPLOY_TARGET=s3
  S3_BUCKET=${BUCKET}
  CLOUDFRONT_DISTRIBUTION_ID=${DIST_ID}
EOF
