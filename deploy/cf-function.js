// CloudFront Function (viewer-request) — 디렉토리 인덱스 재작성.
// CloudFront + S3(OAC) REST 오리진은 디렉토리 인덱스를 자동 해석하지 않으므로,
// MkDocs의 디렉토리 URL(use_directory_urls)을 S3 객체 키로 매핑한다.
//   "/foundation/vpc/"  -> "/foundation/vpc/index.html"
//   "/foundation/vpc"   -> "/foundation/vpc/index.html"
//   "/sitemap.xml"      -> 그대로 (확장자 보유)
function handler(event) {
  var request = event.request;
  var uri = request.uri;

  if (uri.endsWith('/')) {
    request.uri = uri + 'index.html';
  } else {
    // 마지막 경로 세그먼트에 점(확장자)이 없으면 디렉토리로 간주.
    // 상위 세그먼트의 점에 영향받지 않도록 마지막 세그먼트만 검사한다.
    var lastSeg = uri.substring(uri.lastIndexOf('/') + 1);
    if (lastSeg.indexOf('.') === -1) {
      request.uri = uri + '/index.html';
    }
  }
  return request;
}
