resource "aws_api_gateway_method" "noncompliantapi" {
  authorization = "NONE"
  http_method   = "GET"
}