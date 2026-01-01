output "bucket_name" {
  description = "Nom du bucket S3"
  value       = aws_s3_bucket.mlops_bucket.bucket
}

output "bucket_arn" {
  description = "ARN du bucket S3"
  value       = aws_s3_bucket.mlops_bucket.arn
}
