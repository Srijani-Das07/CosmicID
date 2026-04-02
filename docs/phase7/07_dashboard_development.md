# Phase 7: Dashboard Development

## Overview

Two dashboards were developed for CosmicID:
1. **Model Performance Dashboard** (`results.html`) - Static visualization of model metrics
2. **Live Prediction Dashboard** (`live_prediction.html`) - Real-time classification using trained models

---

## Dashboard 1: Model Performance (`results.html`)

### Purpose
Display static performance metrics for all three models: Random Forest, XGBoost, and PRISM.

### Features

| Section | Content |
|---------|---------|
| **Model Selector** | Toggle between PRISM, XGBoost, Random Forest |
| **Metrics Strip** | Test Accuracy, Validation Accuracy, Weighted Precision, Weighted Recall |
| **Confusion Matrix** | Tabular display with highlighted diagonal (correct predictions) |
| **Feature Importance** | Horizontal bar chart showing top 10 features |
| **Per-Class Metrics** | Precision, Recall, F1-Score for GALAXY, QSO, STAR |

### Visual Design

- **Color Palette**: Dark theme with cyan (#00d4ff), purple (#8b5cf6), yellow (#ffd93d), green (#00ff9d)
- **Typography**: IBM Plex Sans Condensed + Share Tech Mono
- **Layout**: Two-column grid with responsive design

### Key Metrics Displayed

| Model | Test Accuracy | GALAXY F1 | QSO F1 | STAR F1 |
|-------|---------------|-----------|--------|---------|
| Random Forest | 97.82% | 0.98 | 0.95 | 0.99 |
| XGBoost | 97.85% | 0.98 | 0.95 | 0.99 |
| **PRISM** | **98.04%** | **0.98** | **0.95** | **1.00** |

---

## Dashboard 2: Live Prediction (`live_prediction.html`)

### Purpose
Allow users to input photometric data and receive real-time predictions from all three models.

### Features

| Feature | Description |
|---------|-------------|
| **Input Form** | 10 fields for SDSS photometric features (u,g,r,i,z, redshift, color indices) |
| **Sample Buttons** | One-click load of STAR, GALAXY, QSO examples |
| **Feature Guide** | Expandable side panel with detailed feature descriptions |
| **Run Prediction** | Sends data to Flask API and displays results |
| **Results Display** | Three-column layout with circular confidence gauges and probability tables |
| **Download** | Export predictions as CSV |

### API Integration

The dashboard communicates with `app_api.py` via REST endpoints:

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/health` | GET | Check API status |
| `/predict` | POST | Send features, receive predictions |

### Sample Request/Response

**Request:**
```json
{
    "uv": 21.74669,
    "green": 20.03493,
    "red": 19.17553,
    "near_ir": 18.81823,
    "ir": 18.65422,
    "redshift": -0.000008,
    "ug": 1.71176,
    "gr": 0.85940,
    "ri": 0.35730,
    "iz": 0.16401
}

**Response:**
{
    "success": true,
    "predictions": {
        "rf": {"prediction": "STAR", "confidence": 92.3, "probabilities": {...}},
        "xgb": {"prediction": "STAR", "confidence": 94.1, "probabilities": {...}},
        "prism": {"prediction": "STAR", "confidence": 96.2, "probabilities": {...}}
    }
}
```

## Central Landing Page (index.html)

### Purpose
- Serve as the entry point for both dashboards.

### Features

- Element Description
- Animated Hero	Gradient "COSMICID" with 3D floating particles
- **Two Cards:** Model Performance → results.html, Live Prediction → live_prediction.html
- API Status Indicator	(Visual check if Flask backend is running)

### Visual Design

- **Background:** Radial gradient with floating particle animation
- **Card Effects:** Glass morphism, 3D hover transforms, glow borders
- **Typography:** Exo 2 + Share Tech Mono

## Flask Backend (app_api.py)

### Purpose
- Load trained models and serve predictions via REST API.

### Endpoints
| Endpoint  | Method | Description |
|-----------|--------|-------------|
|/health|	|GET|	Returns {"status": "ok"}
|/predict	|POST|	Accepts 10 features, returns predictions from all 3 models|
|/model_performance	|GET |Returns static performance metrics |
|/test_star | GET|	Test endpoint with known star sample |

### Model Loading

```
# Models loaded at startup
rf_model = joblib.load('models/random_forest_baseline.pkl')
xgb_model = joblib.load('models/xgboost_model.pkl')
prism_pipeline = joblib.load('models/prism_model.pkl')
scaler = joblib.load('models/scaler.pkl')
label_encoder = joblib.load('models/label_encoder.pkl')
```
### Prediction Pipeline for PRISM

```
Raw Input → Scale → Graph Encoder → Attention → LightGBM → Prediction
```

### File Structure

```
C:\CosmicID\
│
├── index.html              # Central landing page
├── results.html            # Model performance dashboard
├── live_prediction.html    # Live prediction dashboard
├── app_api.py              # Flask backend
├── requirements.txt        # Python dependencies
├── runtime.txt             # Python version for deployment
├── Procfile                # Render startup command
│
├── models/                 # Trained models
│   ├── random_forest_baseline.pkl
│   ├── xgboost_model.pkl
│   ├── prism_model.pkl
│   ├── scaler.pkl
│   └── label_encoder.pkl
│
├── visualizations/         # EDA plots
└── docs/                   # Documentation
```



