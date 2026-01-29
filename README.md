# ASTERRA DevOps Technical Assignment


 I built a GIS data processing microservice in Python,
 running in a container on ECS Fargate,
 processing GeoJSON files using GeoPandas and storing them in PostGIS as
 part of an event-driven data pipeline.
 
> **Design Only – Production Grade Architecture**  
> This project is implemented as a design-only system.  
> No real cloud resources were created, but all components are designed  
> as a real production-grade DevOps architecture.

## Phases
- Phase 0 – Repository & Structure
- Phase 1 – Infrastructure as Code (Terraform)
- Phase 2 – Application & Container Image
- Phase 3 – ECS Deployment Design
- Phase 4 – CI/CD & Documentation

---

## Architecture 
- GeoJSON uploaded to S3  
- Event sent to SQS  
- ECS Fargate runs processing microservice  
- GeoPandas validates and processes data  
- Data stored in PostgreSQL (PostGIS)  

---

## Stack
- Python + Flask  
- GeoPandas / PostGIS  
- Docker  
- ECS Fargate  
- Terraform (IaC)  
- GitHub Actions (CI/CD)  

---

## Phase 0 – Repository & Structure
- Git repository initialization  
- Clear folder separation:
  - `infra/` – Infrastructure  
  - `app/` – Application  
  - `deploy/` – Deployment  
  - `.github/workflows/` – CI/CD  
  - `docs/` – Documentation  

---

## Phase 1 – Infrastructure (IaC)
- VPC with public & private subnets  
- S3 bucket for GeoJSON  
- SQS for event-driven processing  
- PostgreSQL with PostGIS  
- ECS Cluster  
- IAM roles and security groups  
- All defined using Terraform  

---

## Phase 2 – Application / Image
- Python microservice (Flask Worker)  
- Reads messages from SQS  
- Downloads GeoJSON from S3  
- Processes using GeoPandas  
- Stores results in PostGIS  
- Docker image built for ECS  

---

## Phase 3 – Deployment (ECS / Fargate)
- ECS Task Definition  
- ECS Service  
- Fargate (serverless containers)  
- Private networking  
- Secrets injected at runtime  
- Centralized logging  
- Health checks  

---

## Phase 4 – CI/CD + Docs
- GitHub Actions pipeline:
  - Lint  
  - Tests  
  - Build image  
  - Version tagging  
  - Deploy (design)  
- Architecture diagrams  
- Technical documentation  
- Half-page professional summary  

---

## Key Concepts
- Event-driven data pipeline  
- Microservice architecture  
- Infrastructure as Code  
- Serverless containers  
- Observability & Security  

---

## Deployment Flow
Git push → CI/CD → Docker build → ECS update  

---

## One-Line Summary
A production-grade event-driven GIS processing microservice running on ECS Fargate with full DevOps automation.
