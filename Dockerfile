# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run the pipeline script as the first step
RUN python pipeline.py --train_path data/train.csv --test_path data/test.csv --learning_rate 0.01 --n_estimators 300 --max_depth 5 --loss absolute_error


# Define environment variable
ENV PYTHONUNBUFFERED=1

# Command to run the FastAPI server
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
