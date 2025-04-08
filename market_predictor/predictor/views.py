from django.shortcuts import render
import pandas as pd
import pickle
import os
from django.conf import settings

def load_model():
    try:
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        with open(os.path.join(base_dir, 'market_model.pkl'), 'rb') as f:
            model = pickle.load(f)
        with open(os.path.join(base_dir, 'scaler.pkl'), 'rb') as f:
            scaler = pickle.load(f)
        return model, scaler
    except Exception as e:
        print(f"Error loading model: {str(e)}")
        return None, None

def predict_trend(df, model, scaler):
    input_scaled = scaler.transform(df)
    prediction = model.predict(input_scaled)[0]
    probabilities = model.predict_proba(input_scaled)[0]
    
    trend_map = {0: 'Bearish', 1: 'Stable', 2: 'Bullish'}
    return {
        'trend': trend_map[prediction],
        'probabilities': {
            'Bearish': float(probabilities[0]),
            'Stable': float(probabilities[1]),
            'Bullish': float(probabilities[2])
        }
    }

def prediction_form(request):
    context = {'error': None, 'result': None}
    
    if request.method == 'POST':
        try:
            input_data = {
                'Open': float(request.POST.get('open')),
                'High': float(request.POST.get('high')),
                'Low': float(request.POST.get('low')),
                'Close': float(request.POST.get('close')),
                'Volume': float(request.POST.get('volume')),
                'Market_Cap': float(request.POST.get('market_cap')),
                'PE_Ratio': float(request.POST.get('pe_ratio')),
                'Dividend_Yield': float(request.POST.get('dividend_yield')),
                'Volatility': float(request.POST.get('volatility')),
                'Sentiment_Score': float(request.POST.get('sentiment_score')),
                'MA5': float(request.POST.get('ma5')),
                'MA20': float(request.POST.get('ma20'))
            }
            
            input_data['Price_Range'] = input_data['High'] - input_data['Low']
            input_data['Price_Change'] = input_data['Close'] - input_data['Open']
            
            df = pd.DataFrame([input_data])
            model, scaler = load_model()
            
            if model is None or scaler is None:
                context['error'] = 'Error loading model. Please try again.'
                return render(request, 'predictor/form.html', context)
            
            result = predict_trend(df, model, scaler)
            return render(request, 'predictor/result.html', {'result': result})
            
        except ValueError:
            context['error'] = 'Please enter valid numerical values'
        except Exception as e:
            context['error'] = f'An error occurred: {str(e)}'
    
    return render(request, 'predictor/form.html', context)
