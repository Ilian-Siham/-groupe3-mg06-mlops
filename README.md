# 🚀 Infrastructure MLOps - G0MG00

Projet MLOps de déploiement d'une application d'analyse de profil Data/AI avec Terraform et AWS ECS.

## 📋 Services AWS utilisés

| Service | Nom ressource | Rôle |
|---------|--------------|------|
| S3 | `s3-g0mg00` | Stockage des modèles ML et données |
| ECR | `ecr-g0mg00` | Registry Docker pour les images |
| ECS | `ecs-g0mg00` | Orchestration des conteneurs Fargate |
| IAM | `ecs-g0mg00-*-role` | Rôles pour l'exécution des tâches |

## 🏗️ Architecture

```
┌─────────────┐
│   GitHub    │
│   Actions   │
└──────┬──────┘
       │
       ├─► Build Docker Image
       │
       ├─► Push to ECR
       │   (ecr-g0mg00)
       │
       └─► Deploy to ECS
           (ecs-g0mg00)
           │
           ├─► Task Definition
           ├─► Fargate Service
           └─► Public IP
               │
               ├─► API (port 8000)
               └─► Streamlit (port 8501)
```

## 📁 Structure du projet

```
.
├── .github/workflows/
│   ├── test-aws.yml       # Test connexion AWS
│   └── deploy.yml         # Pipeline CI/CD complet
├── modules/
│   ├── s3/               # Module S3
│   ├── ecr/              # Module ECR
│   └── ecs/              # Module ECS + IAM
├── src/
│   ├── api/              # API FastAPI
│   ├── UI/               # Interface Streamlit
│   ├── Database/         # Pipeline de données
│   └── Model/            # Pipeline ML
├── main.tf
├── variables.tf
├── outputs.tf
├── Dockerfile
└── requirements.txt
```

## 🛠️ Installation et déploiement

### 1. Prérequis

- Compte AWS actif
- GitHub repository
- Secrets GitHub configurés :
  - `AWS_ACCESS_KEY_ID`
  - `AWS_SECRET_ACCESS_KEY`
  - `AWS_REGION` (eu-west-3)

### 2. Déploiement automatique

Le déploiement se fait automatiquement via GitHub Actions :

```bash
git add .
git commit -m "Deploy infrastructure"
git push origin main
```

Le workflow :
1. ✅ Crée l'infrastructure Terraform (S3, ECR, ECS)
2. 🐳 Build l'image Docker
3. 📤 Push vers ECR
4. 🚀 Déploie sur ECS Fargate

### 3. Déploiement manuel (optionnel)

```bash
# Initialiser Terraform
terraform init

# Vérifier le plan
terraform plan

# Appliquer
terraform apply

# Build et push Docker
aws ecr get-login-password --region eu-west-3 | docker login --username AWS --password-stdin <account-id>.dkr.ecr.eu-west-3.amazonaws.com
docker build -t ecr-g0mg00 .
docker tag ecr-g0mg00:latest <account-id>.dkr.ecr.eu-west-3.amazonaws.com/ecr-g0mg00:latest
docker push <account-id>.dkr.ecr.eu-west-3.amazonaws.com/ecr-g0mg00:latest
```

## 🎯 Application

L'application est une plateforme d'analyse de profil Data/AI qui :

1. **Collecte** les compétences via un questionnaire
2. **Analyse** le profil avec un modèle sémantique (Sentence Transformers)
3. **Recommande** les métiers correspondants
4. **Visualise** les résultats avec des graphiques interactifs

### Technologies utilisées

- **Backend** : FastAPI
- **Frontend** : Streamlit
- **ML** : Sentence Transformers (all-mpnet-base-v2)
- **Data** : Pandas, NLTK
- **Infra** : Terraform, Docker, AWS ECS

## 📊 Accès à l'application

Après déploiement, les URLs sont affichées dans les logs GitHub Actions :

```
API : http://<PUBLIC_IP>:8000
Streamlit : http://<PUBLIC_IP>:8501
```

### Endpoints API

- `GET /health` - Vérifier le statut
- `POST /predict` - Obtenir les recommandations de métiers

## 🔧 Configuration

### Variables Terraform

```hcl
variable "region" {
  default = "eu-west-3"
}
```

### Resources ECS

- **CPU** : 1024 (1 vCPU)
- **Memory** : 2048 MB
- **Type** : Fargate
- **Ports** : 8000 (API), 8501 (Streamlit)

## 🧹 Nettoyage

Pour supprimer toute l'infrastructure :

```bash
terraform destroy
```

## 👥 Équipe

- Ilian ALI BOTO
- Sarah SHAHIN
- Hafsa REDOUANE
- Najlaa ALLIOUI

**Groupe** : G0-MG00

## 📝 License

Projet éducatif - 2025
