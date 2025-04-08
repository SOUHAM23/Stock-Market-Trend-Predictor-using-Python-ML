import pickle
import pandas as pd

def load_model():
    with open('market_model.pkl', 'rb') as f:
        model = pickle.load(f)
    
    with open('scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    
    return model, scaler

def predict_trend(input_data, model, scaler):
    # Scale input data
    input_scaled = scaler.transform(input_data)
    
    # Predict
    prediction = model.predict(input_scaled)[0]
    probabilities = model.predict_proba(input_scaled)[0]
    
    # Convert to trend
    trend_map = {0: 'Bearish', 1: 'Stable', 2: 'Bullish'}
    predicted_trend = trend_map[prediction]
    
    return {
        'trend': predicted_trend,
        'probabilities': {
            'Bearish': float(probabilities[0]),
            'Stable': float(probabilities[1]),
            'Bullish': float(probabilities[2])
        }
    }

def get_test_input():
    return pd.DataFrame([{
        'Open': 100.0,
        'High': 102.0,
        'Low': 99.0,
        'Close': 101.0,
        'Volume': 150000,
        'Market_Cap': 5000000000,
        'PE_Ratio': 20.0,
        'Dividend_Yield': 2.5,
        'Volatility': 0.02,
        'Sentiment_Score': 0.5,
        'MA5': 100.5,
        'MA20': 100.2,
        'Price_Range': 3.0,
        'Price_Change': 1.0
    }])

if __name__ == "__main__":
    # Load model
    model, scaler = load_model()
    
    # Get test input
    test_data = get_test_input()
    
    # Make prediction
    result = predict_trend(test_data, model, scaler)
    
    print("\nPrediction Results:")
    print("-" * 50)
    print(f"Predicted Trend: {result['trend']}")
    print("\nProbabilities:")
    for trend, prob in result['probabilities'].items():
        print(f"{trend}: {prob:.4f}")
