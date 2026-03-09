# Phase 0: Project Setup - CosmicID

## Project Overview
**CosmicID**: An ML-powered classifier for stars, galaxies, and quasars using SDSS photometric data.

## Environment Setup
- **Python version**: 3.13.7
- **Virtual environment**: `venv` (located in project root)
- **Project root**: `C:\CosmicID\`

## Folder Structure Created

C:\CosmicID
│
├── 📁 app/ # Streamlit dashboard (future)
├── 📁 data/
│ ├── 📁 raw/ # Original SDSS data
│ └── 📁 processed/ # Cleaned data for modeling
├── 📁 models/ # Trained models and preprocessing objects
├── 📁 notebooks/ # Jupyter notebooks for each phase
├── 📁 visualizations/ # Saved plots from EDA
├── 📁 venv/ # Virtual environment
├── 📁 docs/ # Project documentation
├── requirements.txt # All dependencies
└── README.md # Project overview (future)

---

## Dependencies Installed

### Core data science
pandas==2.2.3
numpy==2.2.4
matplotlib==3.10.1
seaborn==0.13.2

### Machine learning
scikit-learn==1.6.1
xgboost==2.1.4
tensorflow==2.20.0

### Dashboard
streamlit==1.43.2
plotly==6.0.1

### Utilities
joblib==1.4.2


## Installation Commands
```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Install all dependencies
pip install -r requirements.txt
```

