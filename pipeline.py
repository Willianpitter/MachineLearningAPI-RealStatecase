from src.pipeline.data_preprocessing import load_data, preprocess_data
from src.pipeline.train_model import train_model
from src.pipeline.evaluate_model import evaluate_model, print_metrics
import argparse

def main(train_path: str, test_path: str, categorical_cols: list, target: str, hyperparams: dict):
    print("Loading data")
    train, test = load_data(train_path, test_path)
    print("Preprocessing data")
    train, test, train_cols, preprocessor = preprocess_data(train, test, categorical_cols, target)
    print("Training model")
    pipeline = train_model(train, train_cols, target, preprocessor, hyperparams)
    print("Evalueting data")
    metrics = evaluate_model(pipeline, test, train_cols, target)
    print_metrics(metrics)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train and evaluate property valuation model.")
    parser.add_argument('--train_path', type=str, default='data/train.csv', help='Path to the training data CSV file.')
    parser.add_argument('--test_path', type=str, default='data/test.csv', help='Path to the test data CSV file.')
    parser.add_argument('--learning_rate', type=float, default=0.01, help='Learning rate for GradientBoostingRegressor.')
    parser.add_argument('--n_estimators', type=int, default=300, help='Number of trees for GradientBoostingRegressor.')
    parser.add_argument('--max_depth', type=int, default=5, help='Max depth for GradientBoostingRegressor.')
    parser.add_argument('--loss', type=str, default='absolute_error', help='Loss function for GradientBoostingRegressor.')

    args = parser.parse_args()

    hyperparams = {
        "learning_rate": args.learning_rate,
        "n_estimators": args.n_estimators,
        "max_depth": args.max_depth,
        "loss": args.loss
    }

    main(args.train_path, args.test_path, ["type", "sector"], "price", hyperparams)
