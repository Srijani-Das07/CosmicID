# CosmicID: Astronomical Object Classification

> A machine learning system that classifies stars, galaxies, and quasars from SDSS photometric data using PRISM — a hybrid model combining graph-based feature engineering, instance-adaptive attention, and calibrated gradient boosting.

[Live Demo](https://cosmicid.onrender.com)

---

## Overview

Astronomical surveys like the Sloan Digital Sky Survey (SDSS) capture millions of celestial objects. Classifying these objects as stars, galaxies, or quasars is essential for understanding the universe. Traditional methods rely on spectroscopic data, which is expensive and time-consuming.

This project uses **photometric data** (magnitudes in 5 bands: u,g,r,i,z) to classify objects with machine learning. The proposed **PRISM** hybrid model achieves **98.04% test accuracy**, outperforming both Random Forest and XGBoost baselines.

---

## Models Included

| Model         | Description                                                                 |
|---------------|-----------------------------------------------------------------------------|
| **Random Forest** | Ensemble of decision trees. Baseline model achieving 97.82% accuracy. |
| **XGBoost**       | Gradient boosting classifier. Baseline model achieving 97.85% accuracy. |
| **PRISM**         | Hybrid model combining graph encoder + attention + calibrated LightGBM. Achieves **98.04% accuracy**. |

Detailed model documentation is available in the [`/docs`](docs/) folder.

> ⚠️ Outputs for each of the models are pre-generated and visible in the respective notebooks. Re-running the notebooks separately may produce slightly different results due to randomness in training and data processing.

---

## Model Details

### 1. Random Forest
 
**Overview**  
An ensemble model that builds many decision trees independently and combines their predictions by majority vote. Each tree learns different patterns from random subsets of the data, making the model robust and interpretable. A good baseline for tabular classification tasks.
 
**Strengths**  
- Robust to outliers
- Provides feature importance
- Fast training and inference
 
**Limitations**  
- No instance-adaptive feature weighting
- Uncalibrated probability outputs
 
---
 
### 2. XGBoost
 
**Overview**  
A gradient boosting model that builds trees sequentially, where each new tree corrects the errors of the previous one. Widely used in competitive ML for structured/tabular data due to its speed and strong out-of-the-box performance.
 
**Strengths**  
- Handles class imbalance well
- Better performance than Random Forest (+0.03%)
 
**Limitations**  
- No explicit band relationship modeling
- Poorly calibrated probabilities
 
---
 
### 3. PRISM (Photometric Recognition with Instance-adaptive Self-Attention Mechanism)
 
**Overview**  
A three-stage hybrid pipeline built specifically for photometric classification. First, a graph encoder enriches each spectral band using its astrophysical relationships with neighboring bands. Then, mutual information-based attention reweights features by their relevance to the classification target. Finally, a calibrated LightGBM classifier produces well-calibrated probability outputs — particularly useful for ambiguous QSO/Galaxy boundaries.
 
**Strengths**  
- Captures band co-dependence via graph encoder
- Instance-adaptive feature weighting
- Calibrated probabilities (better for ambiguous QSO/Galaxy boundaries)
- **98.04% accuracy** — best among all models
 
**Limitations**  
- Band relationship graph is fixed using astrophysical priors, not learned from data
- Attention weights are global per feature, not truly instance-adaptive
- Attention and classifier are trained separately, not end-to-end
- Trained only on SDSS data; generalization to other surveys (e.g., DES, LSST) is untested

---

## Dataset

- **Name:** SDSS Stellar Classification Dataset (SDSS DR17)
- **Source:** [Kaggle – Stellar Classification Dataset](https://www.kaggle.com/datasets/fedesoriano/stellar-classification-dataset-sdss17)
- **Size:** 100,000 observations
- **Classes:** GALAXY (59.4%), STAR (21.6%), QSO (19.0%)
- **Features:** 5 photometric bands (u,g,r,i,z), redshift, and derived color indices

---

## Results

| Model | Test Accuracy | GALAXY F1 | QSO F1 | STAR F1 |
|-------|---------------|-----------|--------|---------|
| Random Forest | 97.82% | 0.98 | 0.95 | 0.99 |
| XGBoost | 97.85% | 0.98 | 0.95 | 0.99 |
| **PRISM** | **98.04%** | **0.98** | **0.95** | **1.00** |

PRISM achieves perfect STAR classification (F1 = 1.00) and improves overall accuracy by 0.22% over the Random Forest baseline.

---

## Project Structure

```
CosmicID/
├── app_api.py                        # Flask API server
├── index.html                        # Landing dashboard
├── results.html                      # Model performance dashboard
├── live_prediction.html              # Live prediction dashboard
├── requirements.txt
├── runtime.txt
├── Procfile
├── start.sh
├── notebooks/
│   ├── 01_data_loading.ipynb
│   ├── 02_data_preprocessing.ipynb
│   ├── 03_eda.ipynb
│   ├── 04_random_forest_baseline_model.ipynb
│   ├── 05_xgboost_baseline_model.ipynb
│   ├── 06_prism_hybrid_model.ipynb
│   └── 07_export_for_powerbi.ipynb
├── models/                           # Serialized model files (.pkl)
├── visualizations/                   # Generated plots and figures
└── docs/
    ├── phase0/  00_project_setup.md
    ├── phase1/  01_data_acquisition.md
    ├── phase2/  02_data_loading_and_initial_exploration.md
    ├── phase3/  03_data_preprocessing.md
    ├── phase4/  04_exploratory_data_analysis.md
    ├── phase5/  05_random_forest_baseline_model.md
    │            05_xgboost_baseline_model.md
    ├── phase6/  06_prism_hybrid_model.md
    ├── phase7/  07_dashboard_development.md
    └── phase8/  08_deployment.md

```


---

## How to Run
 
### Prerequisites
 
Python 3.11 or higher required.
 
```bash
python --version
```
 
Step 1 — Clone the Repository
```bash
git clone https://github.com/Srijani-Das07/CosmicID.git
cd CosmicID
```
 
Step 2 — Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```
 
Step 3 — Install Dependencies
```bash
pip install -r requirements.txt
```
 
Step 4 — Run the API Server
```bash
python app_api.py
```
 
Step 5 — Open Dashboard  
Open index.html in your browser.
 
---
 
## Live Demo
 
The project is deployed on Render:
 
- Central Landing: https://cosmicid.onrender.com
- Model Performance: https://cosmicid.onrender.com/results.html
- Live Prediction: https://cosmicid.onrender.com/live_prediction.html
 
---
 
## Technologies Used
 
| Tool | Purpose |
|------|---------|
| Python 3.11 | Core programming language |
| Pandas / NumPy | Data manipulation and preprocessing |
| Scikit-learn | Random Forest, preprocessing, calibration |
| XGBoost | Gradient boosting baseline |
| LightGBM | Final stage classifier for PRISM |
| Flask | API backend for live predictions |
| HTML/CSS/JS | Interactive dashboards |
| Render | Cloud deployment |
 
---
 
## Documentation
 
Detailed phase-wise documentation is available in the /docs folder:
 
| Phase | Description |
|-------|-------------|
| Phase 0 | Project Setup & Environment |
| Phase 1 | Data Acquisition |
| Phase 2 | Data Loading & Exploration |
| Phase 3 | Data Preprocessing |
| Phase 4 | Exploratory Data Analysis |
| Phase 5 | Baseline Models (RF, XGBoost) |
| Phase 6 | PRISM Hybrid Model |
| Phase 7 | Dashboard Development |
| Phase 8 | Deployment |
 
---
 
## Author
 
[Srijani Das](https://github.com/Srijani-Das07)
 
---
 
## License
 
This repository is released under the [MIT License](LICENSE).
