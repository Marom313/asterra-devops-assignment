module "vpc" {
  source = "../../modules/vpc"
}

module "s3" {
  source = "../../modules/s3"
}

module "sqs" {
  source = "../../modules/sqs"
}

module "iam" {
  source = "../../modules/iam"
}

module "rds" {
  source = "../../modules/rds"
  vpc_id = module.vpc.vpc_id
}

module "ecs" {
  source = "../../modules/ecs"
  vpc_id = module.vpc.vpc_id
}
