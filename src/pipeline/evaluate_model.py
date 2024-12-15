import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error, mean_absolute_error
import pandas as pd

def evaluate_model(pipeline, test: pd.DataFrame, test_cols: list, target: str):
    test_predictions = pipeline.predict(test[test_cols])
    test_target = test[target].values

    metrics = {
        "RMSE": np.sqrt(mean_squared_error(test_predictions, test_target)),
        "MAPE": mean_absolute_percentage_error(test_predictions, test_target),
        "MAE": mean_absolute_error(test_predictions, test_target)
    }

    return metrics

def print_metrics(metrics: dict):
    print("RMSE: ", metrics["RMSE"])
    print("MAPE: ", metrics["MAPE"])
    print("MAE : ", metrics["MAE"])
