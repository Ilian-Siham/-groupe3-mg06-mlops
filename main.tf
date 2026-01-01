terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  backend "s3" {
    bucket  = "terraform-state-g0mg00"
    key     = "infrastructure/terraform.tfstate"
    region  = "eu-west-3"
    encrypt = true
  }
}

provider "aws" {
  region = var.region
}

# S3 Bucket Module
module "s3_G0MG00" {
  source      = "./modules/s3"
  bucket_name = "s3-g0mg00"
}

# ECR Repository Module
module "ecr_G0MG00" {
  source    = "./modules/ecr"
  repo_name = "ecr-g0mg00"
}

# ECS Cluster Module
module "ecs_G0MG00" {
  source       = "./modules/ecs"
  cluster_name = "ecs-g0mg00"
}

# App Runner Service Module
# Décommenté quand vous avez une image Docker dans ECR
# module "apprunner_G0MG00" {
#   source       = "./modules/apprunner"
#   service_name = "apprunner-g0mg00"
#   ecr_repo_url = module.ecr_G0MG00.repository_url
# }
