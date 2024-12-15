import logging
from fastapi import FastAPI, HTTPException, Depends, Security
from fastapi.security.api_key import APIKeyHeader

from pydantic import BaseModel
import pandas as pd
import joblib
import os
from dotenv import load_dotenv 
# Load environment variables from .env file 
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("api_logs.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Property Valuation API",
    description="This API predicts the valuation of residential properties based on various features. It uses a trained machine learning model to provide quick and reliable estimates.",
    version="1.0.0"
)

# Define a fixed API key (in a real application, use environment variables or a secrets manager)
API_KEY = os.getenv("API_KEY")
print('API_KEY', API_KEY)
API_KEY_NAME = "access_token"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

# Function to validate API key
def get_api_key(api_key_header: str = Security(api_key_header)):
    if api_key_header == API_KEY:
        return api_key_header
    else:
        raise HTTPException(status_code=403, detail="Could not validate credentials")

class PropertyData(BaseModel):
    type: str
    sector: str
    net_usable_area: float
    net_area: float
    n_rooms: int
    n_bathroom: int
    latitude: float
    longitude: float
    price: float

    class Config:
        schema_extra = {
            "example": {
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
        }

# Load the model and preprocessor when the app starts
model = joblib.load("pipeline_model.pkl")
preprocessor = joblib.load("preprocessor.pkl")

@app.post("/predict", summary="Predict Property Valuation", description="Receive property data and return the predicted valuation.")
def predict_property_value(data: PropertyData, api_key: str = Depends(get_api_key)):
    try:
        logger.info(f"Received data: {data}")
        property_df = pd.DataFrame([data.dict()])
        
        # Apply the same preprocessing to the incoming data
        property_preprocessed = preprocessor.transform(property_df)
        property_preprocessed = pd.DataFrame(property_preprocessed, columns=property_df.columns)
        
        prediction = model.predict(property_preprocessed)
        logger.info(f"Prediction: {prediction[0]}")
        return {"prediction": prediction[0]}
    except Exception as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
