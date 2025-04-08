# Django Application Documentation

## Project Structure

```
market_predictor/
├── manage.py                 # Django management script
├── market_predictor/         # Main project directory
│   ├── __init__.py
│   ├── settings.py          # Project settings
│   ├── urls.py             # Main URL configuration
│   ├── wsgi.py            # WSGI configuration
│   └── asgi.py           # ASGI configuration
└── predictor/              # Predictor app
    ├── __init__.py
    ├── apps.py           # App configuration
    ├── urls.py          # App URL configuration
    ├── views.py        # Views and logic
    └── templates/     # HTML templates
        └── predictor/
            ├── form.html    # Input form
            └── result.html  # Results page
```

## Components

### Views (views.py)
- `prediction_form`: Handles form display and prediction
- `load_model`: Loads the trained model
- `predict_trend`: Makes predictions using the model

### Templates
- `form.html`: User input form for market data
- `result.html`: Displays prediction results

### URLs
- Main URL: `/` - Prediction form
- Admin: `/admin` - Django admin interface

## Local Development Setup

1. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

4. Create superuser (optional)
```bash
python manage.py createsuperuser
```

5. Run development server
```bash
python manage.py runserver
```

## Configuration

Key settings in `settings.py`:
- Debug mode
- Database configuration
- Static files
- Templates
- Installed apps

## Error Handling

The application includes comprehensive error handling for:
- Invalid input data
- Model loading failures
- Prediction errors
