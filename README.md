# Infrastructure MLOps – G3MG06

Projet MLOps de déploiement d’une application d’analyse de profil Data/AI en utilisant Terraform et AWS ECS.

## Services AWS utilisés

| Service | Nom de la ressource        | Rôle                                    |
|--------|----------------------------|-----------------------------------------|
| S3     | `s3-g3mg06-terraform`      | Stockage des modèles ML et des données  |
| ECR    | `ecr-g3mg06-terraform`     | Registry Docker pour les images         |
| ECS    | `ecs-g3mg06-terraform`     | Orchestration des conteneurs Fargate    |
| IAM    | `ecs-g3mg06-*-role`        | Rôles pour l’exécution des tâches       |

## Architecture

```
┌─────────────┐
│   GitHub    │
│   Actions   │
└──────┬──────┘
       │
       ├─► Build Docker Image
       │
       ├─► Push to ECR
       │   (ecr-g3mg06)
       │
       └─► Deploy to ECS
           (ecs-g3mg06)
           │
           ├─► Task Definition
           ├─► Fargate Service
           └─► Public IP
               │
               ├─► API (port 8000)
               └─► Streamlit (port 8501)
```

## Structure du projet

```
.
├── .github/workflows/
│   ├── test-aws.yml       # Test de la connexion AWS
│   └── deploy.yml         # Pipeline CI/CD complet
├── modules/
│   ├── s3/               # Module S3
│   ├── ecr/              # Module ECR
│   └── ecs/              # Module ECS et IAM
├── src/
│   ├── api/              # API FastAPI
│   ├── UI/               # Interface Streamlit
│   ├── Database/         # Pipeline de données
│   └── Model/            # Pipeline Machine Learning
├── main.tf
├── variables.tf
├── outputs.tf
├── Dockerfile
└── requirements.txt
```

## Installation et déploiement

### 1. Prérequis

* Compte AWS actif
* Repository GitHub
* Secrets GitHub configurés :

  * `AWS_ACCESS_KEY_ID`
  * `AWS_SECRET_ACCESS_KEY`
  * `AWS_REGION` (eu-west-3)

### 2. Déploiement automatique

Le déploiement est entièrement automatisé via GitHub Actions.

```bash
git add .
git commit -m "Deploy infrastructure"
git push origin main
```

Le workflow effectue les étapes suivantes :

1. Création de l’infrastructure avec Terraform (S3, ECR, ECS)
2. Build de l’image Docker
3. Push de l’image vers Amazon ECR
4. Déploiement sur ECS Fargate

### 3. Déploiement manuel (optionnel)

```bash
# Initialisation Terraform
terraform init

# Vérification du plan
terraform plan

# Application de l'infrastructure
terraform apply

# Build et push Docker
aws ecr get-login-password --region eu-west-3 | docker login --username AWS --password-stdin <account-id>.dkr.ecr.eu-west-3.amazonaws.com
docker build -t ecr-g3mg06 .
docker tag ecr-g3mg06:latest <account-id>.dkr.ecr.eu-west-3.amazonaws.com/ecr-g3mg06:latest
docker push <account-id>.dkr.ecr.eu-west-3.amazonaws.com/ecr-g3mg06:latest
```

## Application

L’application est une plateforme d’analyse de profil Data/AI qui permet de :

1. Collecter les compétences via un questionnaire
2. Analyser le profil à l’aide d’un modèle sémantique
3. Recommander des métiers adaptés
4. Visualiser les résultats à l’aide de graphiques interactifs

### Technologies utilisées

* Backend : FastAPI
* Frontend : Streamlit
* Machine Learning : Sentence Transformers (all-mpnet-base-v2)
* Data : Pandas, NLTK
* Infrastructure : Terraform, Docker, AWS ECS

## Accès à l’application

Après le déploiement, les URLs sont affichées dans les logs GitHub Actions.

```
API : http://<PUBLIC_IP>:8000
Streamlit : http://<PUBLIC_IP>:8501
```

### Endpoints API

* `GET /health` : Vérification du statut de l’application
* `POST /predict` : Recommandation de métiers

## Configuration

### Variables Terraform

```hcl
variable "region" {
  default = "eu-west-3"
}
```

### Ressources ECS

* CPU : 1024 (1 vCPU)
* Mémoire : 2048 MB
* Type : Fargate
* Ports exposés : 8000 (API), 8501 (Streamlit)

## Nettoyage de l’infrastructure

Pour supprimer l’ensemble des ressources AWS :

```bash
terraform destroy
```

## Équipe

* Ilian Ali Boto
* Sarah Shahin
* Hafsa Redouane
* Najlaa Alliouui

Groupe : G3MG06

## Licence

Projet éducatif – 2025

