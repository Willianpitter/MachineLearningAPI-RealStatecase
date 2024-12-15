FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "pipeline.py","--train_path data/train.csv", "--test_path data/test.csv", "--learning_rate 0.05", "--n_estimators 500", "--max_depth 4", "--loss absolute_error"]
