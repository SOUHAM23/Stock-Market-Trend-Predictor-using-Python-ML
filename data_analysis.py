import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

def analyze_market_data(data_path):
    # Read data
    data = pd.read_csv(data_path)
    
    # Basic statistics
    print("\nBasic Statistics:")
    print("-" * 50)
    print(data.describe())
    
    # Correlation analysis
    plt.figure(figsize=(12, 8))
    correlation = data[['Open', 'Close', 'Volume', 'PE_Ratio', 'Volatility', 'Sentiment_Score']].corr()
    sns.heatmap(correlation, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.savefig('correlation_matrix.png')
    plt.close()
    
    # Trend distribution
    plt.figure(figsize=(10, 6))
    trend_dist = data['Trend'].value_counts().plot(kind='bar')
    plt.title('Distribution of Market Trends')
    plt.xlabel('Trend')
    plt.ylabel('Count')
    plt.savefig('trend_distribution.png')
    plt.close()
    
    # Volume vs Price
    plt.figure(figsize=(10, 6))
    plt.scatter(data['Volume'], data['Close'])
    plt.title('Volume vs Price')
    plt.xlabel('Volume')
    plt.ylabel('Closing Price')
    plt.savefig('volume_price_scatter.png')
    plt.close()
    
    # Sector analysis
    plt.figure(figsize=(12, 6))
    sector_trend = pd.crosstab(data['Sector'], data['Trend'])
    sector_trend.plot(kind='bar', stacked=True)
    plt.title('Trends by Sector')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('sector_trends.png')
    plt.close()
    
    # Statistical tests
    print("\nStatistical Tests:")
    print("-" * 50)
    
    # Test for normality of returns
    returns = data['Close'].pct_change().dropna()
    _, p_value = stats.normaltest(returns)
    print(f"Returns normality test p-value: {p_value}")
    
    # Test for correlation between sentiment and trend
    sentiment_trend_corr = stats.pointbiserialr(
        data['Sentiment_Score'],
        (data['Trend'] == 'Bullish').astype(int)
    )
    print(f"Sentiment-Trend correlation: {sentiment_trend_corr.correlation:.4f}")
    
    return data

if __name__ == "__main__":
    analyze_market_data('huha.csv')
