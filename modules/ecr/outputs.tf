output "repository_url" {
  description = "URL du repository ECR"
  value       = aws_ecr_repository.mlops_repo.repository_url
}

output "repository_arn" {
  description = "ARN du repository ECR"
  value       = aws_ecr_repository.mlops_repo.arn
}

output "repository_name" {
  description = "Nom du repository ECR"
  value       = aws_ecr_repository.mlops_repo.name
}
