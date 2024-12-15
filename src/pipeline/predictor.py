import pandas as pd

def predict(pipeline, property_data: pd.DataFrame):
    predictions = pipeline.predict(property_data)
    return predictions
