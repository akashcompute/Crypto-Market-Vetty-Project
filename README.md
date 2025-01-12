# **Crypto Market Vetty Project**

A Flask-based REST API application to fetch cryptocurrency market updates from the CoinGecko API. The application provides endpoints to list coins, categories, and detailed information about specific coins while offering robust documentation and testing.

---

## **Features**
- 🚀 List all cryptocurrencies with pagination.
- 📂 Fetch cryptocurrency categories.
- 💰 Retrieve market data for a specific coin (priced in Canadian Dollars).
- 📜 Swagger UI for API documentation.
- ✅ Unit testing with `pytest`.
- 📏 Follows best practices (PEP 8, modular structure).
- 🐳 Dockerized for easy deployment.
- 🔍 Includes linting with `flake8`.

---

## **Requirements**
- **Python**: 3.9

### **Python Libraries**
- Flask
- Flasgger
- Requests
- Pytest
- Flake8

---

## **Installation**

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/crypto-market-vetty-project.git
cd crypto-market-vetty-project
```

### 2. Set Up Virtual Environment
```bash
make venv
```

### 3. Install Dependencies
```bash
make install
```

---

## **Running the Application**

### Run Locally
```bash
make run
```
The application will be accessible at: \
http://localhost:5000

---

## **API Endpoints**

**Base URL**: http://localhost:5000/api/v1

| Endpoint       | Method | Description                                |
|----------------|--------|--------------------------------------------|
| /coins         | GET    | List all cryptocurrencies with pagination. |
| /categories    | GET    | List all cryptocurrency categories.        |
| /coins/<coin_id> | GET  | Fetch details about a specific coin.       |
| /health        | GET    | Health check endpoint.                     |
| /version       | GET    | Get application version.                   |

---

## **API Documentation**

Swagger UI is available at:
http://localhost:5000/apidocs

---

## **Testing**

### Run Unit Tests
```bash
make test
```

### Run Linter
```bash
make lint
```

---

## **Docker Support**

### Build Docker Image
```bash
make build
```

### Run Docker Container
```bash
make up
```

### Stop Docker Container
```bash
make stop
```

### Destroy Docker Container
```bash
make clean
```

---

## **Environment Variables**

Create a .env file at the root of the project to store sensitive information. Example .env file:
```bash
FLASK_ENV=development
COINGECKO_API_URL=https://api.coingecko.com/api/v3
```

---

## **Folder Structure**
    
```plaintext
.
├── Dockerfile
├── Makefile
├── README.md
├── app
│  ├── __init__.py
│  ├── config.py
│  ├── routes.py
│  └── utils.py
├── docker-compose.yaml
├── main.py
├── requirements.txt
├── resources
│   └── swagger.yaml
└── tests
    └── tests_app.py
```

---

## **Contributing**

Contributions are welcome! Please refer to the project's style guide and branch structure.

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

