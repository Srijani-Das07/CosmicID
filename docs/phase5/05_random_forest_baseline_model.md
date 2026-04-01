# Phase 5.1: Baseline Models - Random Forest

## Notebook
- **File**: `notebooks/04_random_forest_baseline_model.ipynb`
- **Kernel**: `venv` (Python 3.13.7)

## Model Configuration
- **Algorithm**: Random Forest Classifier
- **Parameters**:
  - `n_estimators`: 100 trees
  - `max_depth`: 10 (limit overfitting)
  - `random_state`: 42 (reproducibility)
  - `n_jobs`: -1 (use all CPU cores)

## Performance Summary

### Overall Accuracy
| Dataset | Accuracy | Misclassification Rate |
|---------|----------|------------------------|
| **Validation** | 97.87% | 2.13% |
| **Test** | 97.82% | 2.18% |

*Excellent consistency between validation and test sets - no overfitting!*

### Per-Class Performance (Test Set)

| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| **GALAXY** | 0.98 | 0.98 | 0.98 | 8,916 |
| **QSO** | 0.96 | 0.94 | 0.95 | 2,844 |
| **STAR** | 0.99 | 1.00 | 0.99 | 3,239 |

**Key Observations:**
- **STAR** classification is nearly perfect (99% F1)
- **QSO** has slightly lower recall (94%) - most challenging class
- **GALAXY** performs consistently well

## Feature Importance Analysis

### Top 10 Features by Importance

| Rank | Feature | Importance | Insights |
|------|---------|------------|----------------|
| **1** | **red_shift** | **54.7%** | ✅ "Redshift is dominant discriminator" |
| 2 | g-r | 13.1% | ✅ Color indices help |
| 3 | r-i | 11.4% | ✅ Color indices help |
| 4 | u-g | 4.7% | ✅ Color indices help |
| 5 | i-z | 4.4% | ✅ Color indices help |
| 6 | IR_filter | 3.4% | |
| 7 | green_filter | 3.0% | |
| 8 | red_filter | 2.2% | |
| 9 | near_IR_filter | 1.8% | |
| 10 | UV_filter | 1.5% | |

**Key Insight:** Redshift alone accounts for **over 50%** of the model's decision-making power

## Confusion Matrix Analysis

|  | **Predicted GALAXY** | **Predicted QSO** | **Predicted STAR** |
|---|---|---|---|
| **Actual GALAXY** | 8828 | 83 | 5 |
| **Actual QSO** | 145 | 2677 | 22 |
| **Actual STAR** | 1 | 0 | 3238 |


**Misclassification Patterns:**
- **Total errors**: 327 out of 14,999 (2.18%)
- **Main confusion**: QSO ↔ GALAXY (145 + 83 = 228 errors, 70% of all mistakes)
- **STAR misclassifications**: Almost none (only 6 total)

**Why QSO-GALAXY confusion?**
- Overlapping redshift ranges (z≈0.5-1.0)
- Similar photometric properties in some cases
- Confirms that quasars are most challenging

## Error Analysis

Sample misclassifications from test set:

1. QSO → GALAXY
2. GALAXY → QSO
3. QSO → GALAXY
4. QSO → GALAXY
5. GALAXY → STAR (rare case)


## Files Saved

| File | Description |
|------|-------------|
| `models/random_forest_baseline.pkl` | Trained Random Forest model |
| `models/baseline_results.csv` | Performance metrics summary |
| `models/feature_importance.csv` | Feature importance rankings |
| `visualizations/rf_confusion_matrix.png` | Confusion matrix plot |
| `visualizations/rf_feature_importance.png` | Feature importance bar chart |

## Key Takeaways for Next Phase

| Finding | Implication for Advanced Models |
|---------|--------------------------------|
| 97.8% accuracy with simple Random Forest | Room for improvement with XGBoost/NN |
| QSO recall (94%) < others | Focus on improving quasar classification |
| Redshift dominates (54.7% importance) | Must keep redshift in all models |
| Color indices help (33% combined) | Engineered features are valuable |

## Summary
- **Baseline Accuracy**: 97.8% with Random Forest
- **Key Feature**: Redshift (54.7% importance) 
- **Challenging Class**: Quasars (94% recall vs 98-99% for others)
- **Confusion Pattern**: QSO ↔ GALAXY (expected from redshift overlap)
