# 📔 Personal Journal App — AWS Serverless

A secure, real-time personal journal web application built entirely on AWS serverless architecture with fully automated CI/CD deployment using GitHub Actions.

## 🏗️ Architecture

```
Browser → CloudFront (HTTPS) → S3 (Frontend)
                ↓
         API Gateway (REST)
                ↓
          Lambda (Python)
                ↓
          DynamoDB (Database)
```

## ⚙️ CI/CD Pipeline

This project uses GitHub Actions for fully automated deployment.

| Trigger | Action |
|---------|--------|
| Push to `Frontend/` | Injects secrets → deploys to S3 → invalidates CloudFront cache |
| Push to `Lambda/` | Python syntax check → deploys to AWS Lambda |

- Bad code is automatically blocked before reaching AWS
- CloudFront cache invalidated on every frontend deployment
- AWS credentials stored securely in GitHub Secrets — never exposed in code

## ☁️ AWS Services Used

| Service | Purpose |
|---------|---------|
| S3 | Frontend hosting |
| CloudFront | HTTPS + CDN delivery |
| API Gateway | REST API endpoints |
| Lambda | Serverless backend logic |
| DynamoDB | NoSQL database |
| Cognito | User authentication |
| CloudWatch | Monitoring + alerts |
| SNS | Email notifications |
| CloudFormation | Infrastructure as Code |
| IAM | Least privilege security |

## 🔐 Security Implementation

- TLS 1.3 encryption in transit
- Amazon Cognito authentication
- Least privilege IAM policies per service
- GitHub Secrets for credential management
- CORS configured on API Gateway
- S3 bucket policy for public read only
- Sensitive config injected at deploy time — never stored in code

## 📊 Monitoring

- CloudWatch dashboard for Lambda metrics
- SNS email alerts for Lambda errors
- CloudWatch logs for API Gateway + Lambda

## 📁 Project Structure

```
journal-app-aws/
├── .github/
│   └── workflows/
│       ├── deploy-frontend.yml  # S3 + CloudFront deployment
│       └── deploy-lambda.yml    # Lambda deployment with syntax check
├── Frontend/
│   └── daily_notes_app.html     # Journal web app
├── Lambda/
│   └── lambda_function.py       # Backend logic (Python 3.14)
└── Infrastructure/
    ├── JournalApp-IaC.yaml      # CloudFormation template
    └── JournalApp-IaC.json      # CloudFormation template
```

## 🚀 Deployment

This project deploys automatically via GitHub Actions on every push.

For manual infrastructure setup:
1. Deploy CloudFormation template from `/Infrastructure` folder
2. Add required values to GitHub Secrets
3. Push code — CI/CD handles the rest

## 🔮 Future Improvements

- Multi-user support with per-user DynamoDB partition
- Real-time updates using API Gateway WebSockets
- Expense tracking module
- Mobile responsive improvements
- Docker containerization
- Terraform infrastructure management

## 👨‍💻 Author

**Ragunathan K**
AWS Solutions Architect Associate (SAA-C03 | 89%)
AWS Cloud Practitioner (CLF-C02 | 100%)
```
