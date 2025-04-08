# Machine Learning Model Documentation

## Overview

The market trend prediction model uses a Random Forest Classifier to predict market trends based on various financial indicators.

## Features Used

- Opening Price
- High Price
- Low Price
- Closing Price
- Volume
- Market Cap
- PE Ratio
- Dividend Yield
- Volatility
- Sentiment Score
- Moving Averages (5-day and 20-day)
- Price Range
- Price Change

## Model Architecture

- Algorithm: Random Forest Classifier
- Number of Trees: 100
- Random State: 42
- Training/Test Split: 80/20

## Model Performance

The model is evaluated using:
- Accuracy Score
- Classification Report
- Confusion Matrix

## File Structure

```
soham/
├── train_model.py         # Model training script
├── test_model.py         # Model testing script
├── market_model.pkl      # Saved model
└── scaler.pkl           # Feature scaler
```

## Usage

```python
from test_model import load_model, predict_trend

# Load model
model, scaler = load_model()

# Make prediction
result = predict_trend(input_data, model, scaler)
```
