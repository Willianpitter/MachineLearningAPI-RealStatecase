import pandas as pd
from category_encoders import TargetEncoder
from sklearn.compose import ColumnTransformer

def load_data(train_path: str, test_path: str) -> (pd.DataFrame, pd.DataFrame):
    train = pd.read_csv(train_path)
    test = pd.read_csv(test_path)
    return train, test

def preprocess_data(train: pd.DataFrame, test: pd.DataFrame, categorical_cols: list, target: str):
    train_cols = [col for col in train.columns if col not in ['id', target]]

    categorical_transformer = TargetEncoder()

    preprocessor = ColumnTransformer(
        transformers=[
            ('categorical', categorical_transformer, categorical_cols)
        ])

    return train, test, train_cols, preprocessor
