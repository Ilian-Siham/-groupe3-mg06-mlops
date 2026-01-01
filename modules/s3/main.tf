resource "aws_s3_bucket" "mlops_bucket" {
  bucket = var.bucket_name

  tags = {
    Name        = var.bucket_name
    Environment = "MLOps"
    Project     = "G0MG00"
  }
}

resource "aws_s3_bucket_versioning" "mlops_versioning" {
  bucket = aws_s3_bucket.mlops_bucket.id

  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "mlops_encryption" {
  bucket = aws_s3_bucket.mlops_bucket.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}
