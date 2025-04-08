import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

def prepare_features(data):
    # Create technical indicators
    data['MA5'] = data.groupby('Company')['Close'].transform(lambda x: x.rolling(window=5).mean())
    data['MA20'] = data.groupby('Company')['Close'].transform(lambda x: x.rolling(window=20).mean())
    data['Price_Range'] = data['High'] - data['Low']
    data['Price_Change'] = data['Close'] - data['Open']
    
    # Convert Trend to numeric
    trend_map = {'Bullish': 2, 'Stable': 1, 'Bearish': 0}
    data['Trend_Numeric'] = data['Trend'].map(trend_map)
    
    features = ['Open', 'High', 'Low', 'Close', 'Volume', 'Market_Cap', 
               'PE_Ratio', 'Dividend_Yield', 'Volatility', 'Sentiment_Score',
               'MA5', 'MA20', 'Price_Range', 'Price_Change']
    
    return data[features], data['Trend_Numeric']

def train_and_save_model(data_path):
    # Load and prepare data
    data = pd.read_csv(data_path)
    X, y = prepare_features(data)
    
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
    print("\nModel Performance:")
    print("-" * 50)
    print(classification_report(y_test, y_pred))
    
    # Save model and scaler
    with open('market_model.pkl', 'wb') as f:
        pickle.dump(model, f)
    
    with open('scaler.pkl', 'wb') as f:
        pickle.dump(scaler, f)
    
    print("\nModel and scaler saved successfully!")

if __name__ == "__main__":
    train_and_save_model('huha.csv')
