output "s3_bucket_name" {
  description = "Name of the S3 bucket"
  value       = module.s3_G0MG00.bucket_name
}

output "ecr_repository_url" {
  description = "URL of the ECR repository"
  value       = module.ecr_G0MG00.repository_url
}

output "ecs_cluster_id" {
  description = "ID of the ECS cluster"
  value       = module.ecs_G0MG00.cluster_id
}

output "ecs_task_execution_role_arn" {
  description = "ARN of the ECS task execution role"
  value       = module.ecs_G0MG00.task_execution_role_arn
}

# output "apprunner_service_url" {
#   description = "URL of the App Runner service"
#   value       = module.apprunner_G0MG00.service_url
# }

# output "apprunner_service_arn" {
#   description = "ARN of the App Runner service"
#   value       = module.apprunner_G0MG00.service_arn
# }
