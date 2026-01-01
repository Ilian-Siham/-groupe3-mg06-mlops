output "cluster_id" {
  description = "ID du cluster ECS"
  value       = aws_ecs_cluster.mlops_cluster.id
}

output "cluster_name" {
  description = "Nom du cluster ECS"
  value       = aws_ecs_cluster.mlops_cluster.name
}

output "cluster_arn" {
  description = "ARN du cluster ECS"
  value       = aws_ecs_cluster.mlops_cluster.arn
}

output "task_execution_role_arn" {
  description = "ARN du rôle d'exécution des tâches"
  value       = aws_iam_role.ecs_task_execution_role.arn
}

output "task_role_arn" {
  description = "ARN du rôle des tâches"
  value       = aws_iam_role.ecs_task_role.arn
}
