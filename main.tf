terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  backend "s3" {
    bucket  = "terraform-state-g3mg06"
    key     = "infrastructure/terraform.tfstate"
    region  = "eu-west-3"
    encrypt = true
  }
}

provider "aws" {
  region = var.region
}

# S3 Bucket Module
module "s3_G3MG06" {
  source      = "./modules/s3"
  bucket_name = "s3-g3mg06-terraform"
}

# ECR Repository Module
module "ecr_G3MG06" {
  source    = "./modules/ecr"
  repo_name = "ecr-g3mg06-terraform"
}

# ECS Cluster Module
module "ecs_G3MG06" {
  source       = "./modules/ecs"
  cluster_name = "ecs-g3mg06-terraform"
}

