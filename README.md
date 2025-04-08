# Market Trend Predictor Project

## Overview
A web-based machine learning application that predicts market trends (Bearish, Stable, Bullish) using historical market data and various technical indicators.

## Documentation Structure

1. [Model Documentation](docs/model.md)
   - Machine Learning Model Details
   - Feature Engineering
   - Model Performance
   - Usage Examples

2. [Web Application](docs/django.md)
   - Django Project Structure
   - Installation Guide
   - API Documentation
   - Frontend Components

3. [Data Pipeline](docs/data_pipeline.md)
   - Data Processing
   - Feature Engineering
   - Input/Output Format
   - Data Flow

4. [Development Guide](docs/development.md)
   - Setup Instructions
   - Development Environment
   - Contributing Guidelines
   - Best Practices

## Project Structure
```
soham/
├── market_predictor/          # Django web application
│   ├── manage.py
│   ├── market_predictor/      # Django project settings
│   └── predictor/            # Main prediction app
├── docs/                     # Documentation files
│   ├── model.md             # ML model documentation
│   ├── django.md            # Django app documentation
│   ├── data_pipeline.md     # Data processing docs
│   └── development.md       # Development guide
├── models/                   # Model files
│   ├── market_model.pkl     # Trained model
│   └── scaler.pkl          # Feature scaler
└── requirements.txt         # Project dependencies
```

## Quick Start Guide

1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/market-predictor.git
cd market-predictor
```

2. **Set Up Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. **Run Django Application**
```bash
cd market_predictor
python manage.py migrate
python manage.py runserver
```

4. **Access the Application**
- Web Interface: http://localhost:8000
- Admin Panel: http://localhost:8000/admin

## Features
- Real-time market trend predictions
- Interactive web interface
- REST API support
- Detailed prediction analytics
- User-friendly input form
- Comprehensive visualization

## Technology Stack
- Python 3.x
- Django
- Scikit-learn
- Pandas
- NumPy
- SQLite



## Contributing
Please read our [Contributing Guidelines](docs/development.md) for details on submitting pull requests.

## Support
For support, please open an issue in the GitHub repository or contact the maintainers.

