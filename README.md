# MLRealStateCase

# Property-Friends Real Estate Valuation

## Overview

This project is a machine learning solution designed to estimate the valuation of residential properties. The goal is to deliver a production-ready system that includes:

- A robust, modularized pipeline for training, evaluating, and deploying the model.
- A REST API to predict property valuations based on input features.
- Logging and basic security for API monitoring and protection.
- Containerized setup using Docker for easy deployment.

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
MachineLearningAPI-RealStatecase/
├── src/
│   ├── api/
│   │   ├── main.py             # FastAPI entry point
│   │   ├── security.py         # API key implementation
│   │   └── logging_config.py   # Logger configuration
│   ├── pipeline/
│   │   ├── data_loader.py      # Handles data loading
│   │   ├── data_preprocessing.py     # Preprocessing and feature engineering
│   │   ├── train_model.py          # Model training and saving
│   │   ├── evaluate_model.py        # Model evaluation
│   │   └── predictor.py        # Model prediction
├── data/
├── Dockerfile                  # Docker setup
├── docker-compose.yml                  # Docker setup
├── pipeline.py                 # Docker setup
├── requirements.txt            # Python dependencies
├── README.md                   # Documentation
└── .env                        # Environment variables for sensitive data
```

---

## Setup Instructions

### Prerequisites

1. Python 3.9+
2. Docker

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Willianpitter/MachineLearningAPI-RealStatecase.git
   ```

2. **Install Dependencies**
Ensure you have the necessary dependencies installed:  
```plaintext
pip install -r requirements.txt

```
3. **Run the Pipeline**
Ensure train.csv and test.csv files are in the data/ directory. Execute the pipeline script to train the model:
```plaintext
python pipeline.py --train_path data/train.csv --test_path data/test.csv --learning_rate 0.01 --n_estimators 300 --max_depth 5 --loss absolute_error
```

3. **Environment Variables**:
   - Create a `.env` file in the root directory with the following content:
     ```plaintext
     API_KEY=your_secure_api_key
     ```

### Running with Docker

1. **Build the Docker Image**:
   ```bash
   docker-compose up --build

   ```
---

## API Usage


### Endpoints

#### **POST /predict/**

- **Description**: Predicts property valuation based on input features.
- **Request Body**:
  ```json
   {
   "type": "apartment",
   "sector": "downtown",
   "net_usable_area": 75.0,
   "net_area": 90.0,
   "n_rooms": 3,
   "n_bathroom": 2,
   "latitude": -33.4489,
   "longitude": -70.6693,
   "price": 300000.0
   }


docker-compose up --build
docker-compose up

**Example**
   - **Full Request Body**:
   ```plaintext

      curl -X 'POST'   'http://localhost:8000/predict'   -H 'accept: application/json'   -H 'Content-Type: application/json'   -H 'access_token: my_secret_api_key'   -d '{
      "type": "apartment",
      "sector": "downtown",
      "net_usable_area": 75.0,
      "net_area": 90.0,
      "n_rooms": 3,
      "n_bathroom": 2,
      "latitude": -33.4489,
      "longitude": -70.6693,
      "price": 300000.0
      }'
   ```
Make predictions via the API:

Use curl or the interactive documentation at http://localhost:8000/docs.
