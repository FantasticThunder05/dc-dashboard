provider "aws" {
  region = "us-east-1"
}

# 1. Repositorio para tu imagen de Docker
resource "aws_ecr_repository" "repo" {
  name         = "dc-dashboard-repo"
  force_delete = true
}

# 2. Cluster de ECS (Fargate)
resource "aws_ecs_cluster" "cluster" {
  name = "dc-cluster"
}

# 3. Network básica (VPC y Subnets)
resource "aws_default_vpc" "default" {}
resource "aws_default_subnet" "default_a" { availability_zone = "us-east-1a" }
resource "aws_default_subnet" "default_b" { availability_zone = "us-east-1b" }