import joblib
from sklearn.pipeline import Pipeline
from sklearn.ensemble import GradientBoostingRegressor
import pandas as pd
def train_model(train: pd.DataFrame, train_cols: list, target: str, preprocessor, hyperparams: dict):
    steps = [
        ('preprocessor', preprocessor),
        ('model', GradientBoostingRegressor(**hyperparams))
    ]

    pipeline = Pipeline(steps)
    pipeline.fit(train[train_cols], train[target])

    # Save the trained pipeline model
    joblib.dump(pipeline, 'pipeline_model.pkl')

    return pipeline
