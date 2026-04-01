# Phase 5.2: Baseline Models - XGBoost

## Notebook
- **File**: `notebooks/05_xgboost_baseline_model.ipynb`
- **Kernel**: `venv` (Python 3.13.7)

## Overview

After establishing a strong baseline with Random Forest (97.82% test accuracy), implemented XGBoost (eXtreme Gradient Boosting) to attempt to improve classification performance. XGBoost is a powerful gradient boosting algorithm known for its performance on tabular data.

---

## Model Configuration

### XGBoost Parameters

```python
xgb_model = xgb.XGBClassifier(
    n_estimators=200,           # Number of trees
    max_depth=6,                # Maximum tree depth (prevents overfitting)
    learning_rate=0.1,          # Step size shrinkage
    subsample=0.8,              # Fraction of samples per tree
    colsample_bytree=0.8,       # Fraction of features per tree
    random_state=42,            # Reproducibility
    use_label_encoder=False,    # Disable deprecated label encoder
    eval_metric='mlogloss'      # Multi-class log loss
)
```

---

## Performance Results

### Overall Accuracy Comparison

| Model | Validation Accuracy | Test Accuracy | Improvement |
|---|---|---|---|
| Random Forest | 97.87% | 97.82% | Baseline |
| XGBoost | 97.92% | 97.85% | +0.03% |

### Per-Class Performance (XGBoost Test Set)

| Class | Precision | Recall | F1-Score | Support |
|---|---|---|---|---|
| GALAXY | 0.98 | 0.98 | 0.98 | 8,916 |
| QSO | 0.96 | 0.95 | 0.95 | 2,844 |
| STAR | 0.99 | 1.00 | 0.99 | 3,239 |

**Key Observations:**
- XGBoost slightly outperforms Random Forest (+0.03%)
- QSO classification improved (recall: 94% → 95%)
- STAR classification remains nearly perfect (99% F1)
- GALAXY maintains consistent 98% performance

---

## Feature Importance Analysis

### Top 10 Features by Importance

| Rank | Feature | XGBoost Importance | Random Forest Importance |
|---|---|---|---|
| 1 | red_shift | 57.0% | 54.7% |
| 2 | r-i | 15.8% | 11.4% |
| 3 | g-r | 8.5% | 13.1% |
| 4 | green_filter | 4.4% | 3.0% |
| 5 | u-g | 4.2% | 4.7% |
| 6 | red_filter | 2.6% | 2.2% |
| 7 | IR_filter | 2.2% | 3.4% |
| 8 | i-z | 1.9% | 4.4% |
| 9 | UV_filter | 1.7% | 1.5% |
| 10 | near_IR_filter | 1.7% | 1.8% |

### Key Insights

- **Redshift Dominance:** Both models agree redshift is the most important feature (~55–57% importance)
- **Color Indices Matter:** r-i, g-r, u-g, i-z collectively account for ~30% of importance
- **Magnitude Filters:** Individual filters contribute less than 5% each
- **Consistency:** Both models rank features similarly, validating feature selection

---

## Confusion Matrix Analysis

```
XGBoost Test Set Confusion Matrix:
                Predicted
              GALAXY   QSO   STAR
Actual GALAXY   8738   173      5
       QSO       121  2715      8
       STAR        1     0   3238
```

**Error Analysis:**
- Total misclassifications: 308 out of 14,999 (2.05%)
- Main confusion: QSO ↔ GALAXY (173 + 121 = 294 errors, 95% of all mistakes)
- STAR misclassifications: Only 6 total (0.04% error rate)
- Improvement: XGBoost reduced QSO misclassifications compared to Random Forest

---

## Model Comparison Visualizations

| Visualization | Path |
|---|---|
| Confusion Matrix | `visualizations/xgb_confusion_matrix.png` |
| Feature Importance Comparison | `visualizations/feature_importance_comparison.png` |
| Model Performance Comparison | `visualizations/model_comparison.png` |

---

## Files Saved

| File | Description |
|---|---|
| `models/xgboost_model.pkl` | Trained XGBoost model |
| `models/xgboost_results.csv` | Performance metrics |
| `models/model_comparison.csv` | Comparison with Random Forest |
| `visualizations/xgb_confusion_matrix.png` | XGBoost confusion matrix |
| `visualizations/feature_importance_comparison.png` | Feature importance comparison |
| `visualizations/model_comparison.png` | Accuracy comparison bar chart |

---

## Key Takeaways

| Finding | Implication |
|---|---|
| XGBoost achieves 97.85% test accuracy | Slightly better than Random Forest |
| Redshift remains dominant (57% importance) | Confirms expectation |
| QSO classification improved | Gradient boosting handles challenging class better |
| Both models show similar feature importance | Validates feature engineering |
| ~2% misclassification rate | Room for improvement with ensemble methods |

---

## Summary

- **XGBoost Test Accuracy:** 97.85% (vs Random Forest 97.82%)
- **Top Feature:** Redshift (57% importance)
- **Best Class:** STAR (99% F1-score)
- **Most Challenging:** QSO (95% F1-score)
- **Main Confusion:** QSO ↔ GALAXY (expected from redshift overlap)

