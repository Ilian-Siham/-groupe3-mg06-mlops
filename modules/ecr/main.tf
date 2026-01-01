resource "aws_ecr_repository" "mlops_repo" {
  name                 = var.repo_name
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }

  tags = {
    Name        = var.repo_name
    Environment = "MLOps"
    Project     = "G0MG00"
  }
}

resource "aws_ecr_lifecycle_policy" "mlops_lifecycle" {
  repository = aws_ecr_repository.mlops_repo.name

  policy = jsonencode({
    rules = [{
      rulePriority = 1
      description  = "Garde les 10 dernières images"
      selection = {
        tagStatus   = "any"
        countType   = "imageCountMoreThan"
        countNumber = 10
      }
      action = {
        type = "expire"
      }
    }]
  })
}
