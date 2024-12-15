# MLRealStateCase

# Property-Friends Real Estate Valuation

## Overview

This project is a machine learning solution designed to estimate the valuation of residential properties in Chile. The goal is to deliver a production-ready system that includes:

- A robust, modularized pipeline for training, evaluating, and deploying the model.
- A REST API to predict property valuations based on input features.
- Logging and basic security for API monitoring and protection.
- Containerized setup using Docker for easy deployment.

The solution is scalable and future-proof, allowing seamless integration with databases for data ingestion.

---

## Features

1. **Pipeline**:
   - Automates data preprocessing, model training, and evaluation.
   - Encapsulates functionality for future database integration.
   - Saves trained models for API use.

2. **API**:
   - Provides property valuation predictions via a RESTful interface.
   - Implements API key authentication for security.
   - Logs API usage for future monitoring and debugging.

3. **Dockerized Deployment**:
   - Ensures consistency and reproducibility across environments.

4. **Scalability**:
   - Modular architecture to easily extend functionalities (e.g., new models, data sources).

---

## Project Structure

```plaintext
property-friends/
├── src/
│   ├── api/
│   │   ├── main.py             # FastAPI entry point
│   │   ├── security.py         # API key implementation
│   │   └── logging_config.py   # Logger configuration
│   ├── pipeline/
│   │   ├── data_loader.py      # Handles data loading
│   │   ├── preprocessor.py     # Preprocessing and feature engineering
│   │   ├── trainer.py          # Model training and saving
│   │   ├── evaluator.py        # Model evaluation
│   │   └── predictor.py        # Model prediction
│   ├── config/
│   │   ├── model_config.py     # Configuration for the model and pipeline
│   │   └── settings.py         # General settings, including placeholders for DB connections
├── tests/
│   ├── test_pipeline.py        # Unit tests for the pipeline
│   ├── test_api.py             # Unit tests for the API
├── Dockerfile                  # Docker setup
├── requirements.txt            # Python dependencies
├── README.md                   # Documentation
└── .env                        # Environment variables for sensitive data
```

---

## Setup Instructions

### Prerequisites

1. Python 3.9+
2. Docker
3. pip (Python package installer)

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Willianpitter/MLRealStateCase.git
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Variables**:
   - Create a `.env` file in the root directory with the following content:
     ```plaintext
     API_KEY=your_secure_api_key
     ```

4. **Run the API Locally**:
   ```bash
   uvicorn src.api.main:app --reload
   ```
   Access the API documentation at `http://127.0.0.1:8000/docs`.

### Running with Docker

1. **Build the Docker Image**:
   ```bash
   docker build -t property-friends-api .
   ```

2. **Run the Container**:
   ```bash
   docker run -p 8000:8000 --env-file .env property-friends-api
   ```

---

## API Usage

### Authentication

All API endpoints require an API key. Pass the key in the `Authorization` header as follows:
```plaintext
Authorization: Bearer <API_KEY>
```

### Endpoints

#### **POST /predict/**

- **Description**: Predicts property valuation based on input features.
- **Request Body**:
  ```json
  {
    "type": "apartment


docker-compose up --build
docker-compose up

curl -X 'POST' \
  'http://localhost:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "type": "apartment",
  "sector": "downtown"
  # add other property features here
}'

Make predictions via the API:

Use curl or the interactive documentation at http://localhost:8000/docs.