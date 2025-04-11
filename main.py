import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data
data = pd.read_csv('data.csv')

def analyze_data(data):
    """Analyze and display market data statistics"""
    print("\nData Analysis:")
    print("-" * 50)
    print(f"Total records: {len(data)}")
    print(f"\nMissing values:\n{data.isnull().sum()}")
    print(f"\nUnique companies: {data['Company'].nunique()}")
    print(f"Unique sectors: {data['Sector'].nunique()}")
    print(f"\nTrend distribution:\n{data['Trend'].value_counts()}")
    
    # Create basic visualizations
    plt.figure(figsize=(12, 6))
    sns.countplot(data=data, x='Trend')
    plt.title('Distribution of Market Trends')
    plt.savefig('trend_distribution.png')
    plt.close()

def prepare_features(data):
    """Prepare features for model training"""
    # Create technical indicators
    data['MA5'] = data.groupby('Company')['Close'].transform(lambda x: x.rolling(window=5).mean())
    data['MA20'] = data.groupby('Company')['Close'].transform(lambda x: x.rolling(window=20).mean())
    data['Price_Range'] = data['High'] - data['Low']
    data['Price_Change'] = data['Close'] - data['Open']
    
    # Convert Trend to numeric
    trend_map = {'Bullish': 2, 'Stable': 1, 'Bearish': 0}
    data['Trend_Numeric'] = data['Trend'].map(trend_map)
    
    # Select features for model
    features = ['Open', 'High', 'Low', 'Close', 'Volume', 'Market_Cap', 
               'PE_Ratio', 'Dividend_Yield', 'Volatility', 'Sentiment_Score',
               'MA5', 'MA20', 'Price_Range', 'Price_Change']
    
    # Handle missing values
    data = data.dropna()
    
    return data[features], data['Trend_Numeric']

def get_user_input():
    """Get input for prediction"""
    print("\nEnter the following market data:")
    try:
        input_data = {
            'Open': float(input("Opening Price: ")),
            'High': float(input("High Price: ")),
            'Low': float(input("Low Price: ")),
            'Close': float(input("Closing Price: ")),
            'Volume': float(input("Volume: ")),
            'Market_Cap': float(input("Market Cap: ")),
            'PE_Ratio': float(input("PE Ratio: ")),
            
            'Dividend_Yield': float(input("Dividend Yield: ")),
            'Volatility': float(input("Volatility: ")),
            'Sentiment_Score': float(input("Sentiment Score (-1 to 1): ")),
            'MA5': float(input("5-day Moving Average: ")),
            'MA20': float(input("20-day Moving Average: ")),
        }
        input_data['Price_Range'] = input_data['High'] - input_data['Low']
        input_data['Price_Change'] = input_data['Close'] - input_data['Open']
        return pd.DataFrame([input_data])
    except ValueError:
        print("Please enter valid numerical values.")
        return None

def train_model(X, y):
    """Train the prediction model"""
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)
    
    # Evaluate model
    y_pred = model.predict(X_test_scaled)
    accuracy = accuracy_score(y_test, y_pred)
    
    print("\nModel Performance:")
    print("-" * 50)
    print(f"Accuracy: {accuracy:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    return model, scaler

def predict_trend(model, scaler, input_data):
    """Predict market trend"""
    # Scale input data
    input_scaled = scaler.transform(input_data)
    
    # Make prediction
    prediction = model.predict(input_scaled)[0]
    probabilities = model.predict_proba(input_scaled)[0]
    
    # Convert numeric prediction to trend
    trend_map = {0: 'Bearish', 1: 'Stable', 2: 'Bullish'}
    predicted_trend = trend_map[prediction]
    
    print("\nPrediction Results:")
    print("-" * 50)
    print(f"Predicted Trend: {predicted_trend}")
    print(f"Prediction Probabilities:")
    print(f"Bearish: {probabilities[0]:.2f}")
    print(f"Stable: {probabilities[1]:.2f}")
    print(f"Bullish: {probabilities[2]:.2f}")

def main():
    # Analyze data
    analyze_data(data)
    
    # Prepare and train model
    X, y = prepare_features(data)
    model, scaler = train_model(X, y)
    
    # Prediction loop
    while True:
        print("\nPredict Market Trend")
        print("-" * 50)
        input_data = get_user_input()
        
        if input_data is not None:
            predict_trend(model, scaler, input_data)
        
        if input("Try another prediction? (yes/no): ").lower() != 'yes':
            break

if __name__ == "__main__":
    main()
