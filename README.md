# 📔 Personal Journal App — AWS Serverless

A secure, real-time personal journal web application
built entirely on AWS serverless architecture.

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
- Least privilege IAM policies
- CORS configured on API Gateway
- S3 bucket policy for public read only

## 📊 Monitoring
- CloudWatch dashboard for Lambda metrics
- SNS email alerts for Lambda errors
- CloudWatch logs for API Gateway + Lambda

## 🚀 Deployment
Infrastructure can be recreated using
CloudFormation template in `/infrastructure` folder.

## 📁 Project Structure
```
journal-app-aws/
├── frontend/
│   └── index.html         # Journal web app
├── lambda/
│   └── lambda_function.py # Backend logic
└── infrastructure/
    ├── JournalApp-IaC.yaml # CloudFormation template
    └── JournalApp-IaC.json # CloudFormation template
```

## ⚙️ Setup Instructions
1. Deploy CloudFormation template
2. Update `API_URL` in `frontend/index.html`
3. Update `COGNITO_CONFIG` in `frontend/index.html`
4. Upload `frontend/index.html` to S3 bucket
5. Access via CloudFront URL

## 🔮 Future Improvements
- Multi-user support with per-user DynamoDB partition
- Real-time updates using API Gateway WebSockets
- Expense tracking module
- Mobile responsive improvements

## 👨‍💻 Author
**Ragunathan K**
AWS Solutions Architect Associate (SAA-C03 | 89%)
AWS Cloud Practitioner (CLF-C02 | 100%)
