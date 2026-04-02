"""
CosmicID Flask API - Serves predictions from trained models
Run with: python app_api.py
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import joblib
import json
import os

app = Flask(__name__)
CORS(app)  # Allow requests from HTML dashboard

# Numpy JSON encoder
class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (np.float32, np.float64)):
            return float(obj)
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.bool_):
            return bool(obj)
        return super().default(obj)


# ============================================
# CUSTOM CLASSES 
# ============================================

class ColorGraphEncoder:
    def __init__(self, feature_names):
        self.band_indices = {
            'u': feature_names.index('UV_filter'),
            'g': feature_names.index('green_filter'),
            'r': feature_names.index('red_filter'),
            'i': feature_names.index('near_IR_filter'),
            'z': feature_names.index('IR_filter')
        }
        
        adjacency = np.zeros((5, 5))
        adjacency[0, 1] = adjacency[1, 0] = 1.0
        adjacency[1, 2] = adjacency[2, 1] = 1.0
        adjacency[2, 3] = adjacency[3, 2] = 1.0
        adjacency[3, 4] = adjacency[4, 3] = 1.0
        adjacency[0, 2] = adjacency[2, 0] = 0.5
        adjacency[1, 4] = adjacency[4, 1] = 0.3
        
        row_sums = adjacency.sum(axis=1, keepdims=True)
        self.adjacency_norm = adjacency / row_sums
    
    def transform(self, X):
        band_features = X[:, [self.band_indices['u'], self.band_indices['g'],
                              self.band_indices['r'], self.band_indices['i'],
                              self.band_indices['z']]]
        enriched = band_features @ self.adjacency_norm.T
        X_out = X.copy()
        for i, band in enumerate(['u', 'g', 'r', 'i', 'z']):
            X_out[:, self.band_indices[band]] = enriched[:, i]
        return X_out


class MutualInfoAttention:
    def __init__(self):
        self.weights = None
    
    def transform(self, X):
        return X * self.weights


# ============================================
# LOAD MODELS
# ============================================

print("=" * 50)
print("Loading CosmicID Models...")
print("=" * 50)

# Load Random Forest
rf_model = joblib.load('models/random_forest_baseline.pkl')
print("✓ Random Forest loaded")

# Load XGBoost
xgb_model = joblib.load('models/xgboost_model.pkl')
print("✓ XGBoost loaded")

# Load PRISM pipeline
prism_pipeline = joblib.load('models/prism_model.pkl')
print("✓ PRISM loaded")

# Load feature names and label encoder
feature_names = joblib.load('models/feature_names.pkl')
label_encoder = joblib.load('models/label_encoder.pkl')

print("✓ Feature names and label encoder loaded")
print("=" * 50)

# Class names for output
class_names = label_encoder.classes_.tolist()  # ['GALAXY', 'QSO', 'STAR']


# ============================================
# PREDICTION FUNCTION
# ============================================

def predict_from_input(input_dict):
    """
    Input: dict with keys: uv, green, red, near_ir, ir, redshift, ug, gr, ri, iz
    Returns: predictions from all 3 models
    """
    
    # Create feature array in correct order
    features = [
        input_dict['uv'],      # UV_filter
        input_dict['green'],   # green_filter
        input_dict['red'],     # red_filter
        input_dict['near_ir'], # near_IR_filter
        input_dict['ir'],      # IR_filter
        input_dict['redshift'],# red_shift
        input_dict['ug'],      # u-g
        input_dict['gr'],      # g-r
        input_dict['ri'],      # r-i
        input_dict['iz']       # i-z
    ]
    
    X = np.array(features, dtype=np.float32).reshape(1, -1)
    
    # Random Forest
    rf_pred_idx = rf_model.predict(X)[0]
    rf_proba = rf_model.predict_proba(X)[0]
    rf_confidence = float(rf_proba[rf_pred_idx] * 100)
    
    # XGBoost
    xgb_pred_idx = xgb_model.predict(X)[0]
    xgb_proba = xgb_model.predict_proba(X)[0]
    xgb_confidence = float(xgb_proba[xgb_pred_idx] * 100)
    
    # PRISM (apply graph encoder and attention)
    X_enc = prism_pipeline['graph_encoder'].transform(X)
    X_att = prism_pipeline['attention'].transform(X_enc)
    prism_pred_idx = prism_pipeline['classifier'].predict(X_att)[0]
    prism_proba = prism_pipeline['classifier'].predict_proba(X_att)[0]
    prism_confidence = float(prism_proba[prism_pred_idx] * 100)

    print(f"RF Prediction: {class_names[int(rf_pred_idx)]} ({rf_confidence:.1f}%)")
    print(f"XGB Prediction: {class_names[int(xgb_pred_idx)]} ({xgb_confidence:.1f}%)")
    print(f"PRISM Prediction: {class_names[int(prism_pred_idx)]} ({prism_confidence:.1f}%)")
    
    return {
        'rf': {
            'prediction': class_names[int(rf_pred_idx)],
            'confidence': rf_confidence,
            'probabilities': {
                'GALAXY': float(rf_proba[0] * 100),
                'QSO': float(rf_proba[1] * 100),
                'STAR': float(rf_proba[2] * 100)
            }
        },
        'xgb': {
            'prediction': class_names[int(xgb_pred_idx)],
            'confidence': xgb_confidence,
            'probabilities': {
                'GALAXY': float(xgb_proba[0] * 100),
                'QSO': float(xgb_proba[1] * 100),
                'STAR': float(xgb_proba[2] * 100)
            }
        },
        'prism': {
            'prediction': class_names[int(prism_pred_idx)],
            'confidence': prism_confidence,
            'probabilities': {
                'GALAXY': float(prism_proba[0] * 100),
                'QSO': float(prism_proba[1] * 100),
                'STAR': float(prism_proba[2] * 100)
            }
        }
    }


# ============================================
# API ENDPOINTS
# ============================================

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok', 'models_loaded': True})


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        
        # DEBUG: Print what we received
        print("\n" + "="*50)
        print("Received data from frontend:")
        print(data)
        print("="*50)
        
        input_dict = {
            'uv': float(data.get('uv', 0)),
            'green': float(data.get('green', 0)),
            'red': float(data.get('red', 0)),
            'near_ir': float(data.get('near_ir', 0)),
            'ir': float(data.get('ir', 0)),
            'redshift': float(data.get('redshift', 0)),
            'ug': float(data.get('ug', 0)),
            'gr': float(data.get('gr', 0)),
            'ri': float(data.get('ri', 0)),
            'iz': float(data.get('iz', 0))
        }
        
        print("Parsed input_dict:", input_dict)
        
        predictions = predict_from_input(input_dict)
        
        print("Predictions:", predictions)
        
        return jsonify({
            'success': True,
            'predictions': predictions
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/model_performance', methods=['GET'])
def model_performance():
    """Return static model performance metrics"""
    return jsonify({
        'prism': {'test_accuracy': 0.9804, 'validation_accuracy': 0.9747},
        'xgboost': {'test_accuracy': 0.9785, 'validation_accuracy': 0.9792},
        'random_forest': {'test_accuracy': 0.9782, 'validation_accuracy': 0.9787}
    })


# ============================================
# RUN SERVER
# ============================================

if __name__ == '__main__':
    print("\n" + "=" * 50)
    print("CosmicID API Server Running")
    print("=" * 50)
    print("Endpoint: http://localhost:5000")
    print("POST /predict - Send features for classification")
    print("GET /health - Check server status")
    print("=" * 50 + "\n")
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

