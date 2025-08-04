# AI Personal Finance Manager

An intelligent personal finance application that processes receipts using AI to automatically categorize expenses and track spending patterns.

## 🚀 Features

- **Receipt Processing**: Upload receipt images and extract text using AWS Textract
- **AI Categorization**: Automatically categorize expenses using Amazon Bedrock/Claude
- **Transaction Storage**: Store and manage transactions in DynamoDB
- **Modern UI**: React frontend with Vite for fast development
- **Serverless Backend**: Python Lambda functions with API Gateway

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   React Frontend│    │  API Gateway    │    │  Lambda Function│
│   (Vite)        │◄──►│                 │◄──►│  (Python)       │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                                       │
                                                       ▼
                       ┌─────────────────┐    ┌─────────────────┐
                       │   DynamoDB      │    │  AWS Textract   │
                       │   (Transactions)│    │  (OCR)          │
                       └─────────────────┘    └─────────────────┘
                                                       │
                                                       ▼
                                              ┌─────────────────┐
                                              │ Amazon Bedrock  │
                                              │ (AI Categorization)│
                                              └─────────────────┘
```

## 📁 Project Structure

```
ai-personal-finance/
├── backend/                    # Python Lambda backend
│   ├── lambda_function.py     # Main Lambda handler
│   ├── receipt_processor.py   # Text extraction logic
│   ├── transaction_categorizer.py # AI categorization
│   ├── data_storage.py        # DynamoDB operations
│   ├── utils/                 # Helper functions
│   │   ├── aws_helpers.py     # AWS service clients
│   │   └── response_helpers.py # API response helpers
│   ├── requirements.txt       # Python dependencies
│   └── tests/                 # Unit tests
├── frontend/                  # React frontend
│   ├── src/                   # React components
│   ├── public/                # Static assets
│   └── package.json           # Node.js dependencies
├── aws-infrastructure/        # AWS infrastructure
│   └── template.yaml          # SAM template
├── .gitignore                 # Git ignore rules
└── README.md                  # This file
```

## 🛠️ Tech Stack

### Backend
- **Python 3.11**: Lambda runtime
- **AWS Lambda**: Serverless compute
- **AWS Textract**: OCR for receipt processing
- **Amazon Bedrock**: AI-powered categorization
- **DynamoDB**: NoSQL database for transactions
- **API Gateway**: REST API endpoints

### Frontend
- **React 18**: UI framework
- **TypeScript**: Type safety
- **Vite**: Build tool and dev server
- **Axios**: HTTP client

### Infrastructure
- **AWS SAM**: Serverless deployment
- **CloudFormation**: Infrastructure as Code

## 🚀 Getting Started

### Prerequisites

1. **AWS Account**: Set up with appropriate permissions
2. **AWS CLI**: Configured with your credentials
3. **Node.js**: Latest LTS version
4. **Python**: 3.11 or later
5. **AWS SAM CLI**: For deployment

### Installation

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd ai-personal-finance
   ```

2. **Set up the backend**:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. **Set up the frontend**:
   ```bash
   cd frontend
   npm install
   ```

### AWS Setup

1. **Configure AWS credentials**:
   ```bash
   aws configure
   ```

2. **Deploy the infrastructure**:
   ```bash
   cd aws-infrastructure
   sam build
   sam deploy --guided
   ```

3. **Note the API Gateway URL** from the deployment output.

### Development

1. **Start the frontend development server**:
   ```bash
   cd frontend
   npm run dev
   ```

2. **Test the backend locally** (optional):
   ```bash
   cd backend
   sam local start-api
   ```

## 📋 API Endpoints

### Process Receipt
```
POST /process-receipt
Content-Type: application/json

{
  "image_data": "base64_encoded_image",
  "user_id": "user123"
}
```

### Get Transactions
```
GET /transactions?user_id=user123&limit=50
```

## 🔧 Configuration

### Environment Variables

The following environment variables are automatically set by SAM:

- `ENVIRONMENT`: Deployment environment (dev/staging/prod)
- `TRANSACTIONS_TABLE_NAME`: DynamoDB table name

### AWS Services Required

- **IAM**: Permissions for Lambda, DynamoDB, S3, Textract, Bedrock
- **DynamoDB**: Transaction storage table
- **S3**: Receipt image storage
- **API Gateway**: REST API endpoints
- **Lambda**: Serverless compute

## 🧪 Testing

### Backend Tests
```bash
cd backend
python -m pytest tests/
```

### Frontend Tests
```bash
cd frontend
npm test
```

## 📦 Deployment

### Backend Deployment
```bash
cd aws-infrastructure
sam build
sam deploy
```

### Frontend Deployment
```bash
cd frontend
npm run build
# Deploy dist/ folder to S3/CloudFront
```

## 🔒 Security

- **CORS**: Configured for cross-origin requests
- **IAM**: Least privilege access policies
- **S3**: Private bucket with lifecycle policies
- **API Gateway**: Request validation and throttling

## 📈 Monitoring

- **CloudWatch Logs**: Lambda function logs
- **CloudWatch Metrics**: API Gateway and Lambda metrics
- **X-Ray**: Distributed tracing (optional)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For questions or issues:
1. Check the documentation
2. Search existing issues
3. Create a new issue with detailed information

## 🗺️ Roadmap

### Phase 1: MVP ✅
- [x] Basic receipt processing
- [x] AI categorization
- [x] Transaction storage
- [x] Simple UI

### Phase 2: Enhanced Features
- [ ] User authentication (Cognito)
- [ ] Receipt image upload to S3
- [ ] Advanced categorization rules
- [ ] Spending analytics

### Phase 3: Advanced Features
- [ ] Budget tracking
- [ ] Recurring expense detection
- [ ] Export functionality
- [ ] Mobile app

---

**Happy coding! 🎉**
