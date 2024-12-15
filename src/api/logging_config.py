import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.post("/predict")
def predict_property_value(data: PropertyData):
    try:
        logger.info(f"Received data: {data}")
        # Preprocess data and load model
        model = joblib.load("pipeline_model.pkl")
        property_df = pd.DataFrame([data.dict()])
        prediction = model.predict(property_df)
        logger.info(f"Prediction: {prediction[0]}")
        return {"prediction": prediction[0]}
    except Exception as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
