# Phase 3: Data Preprocessing

## Notebook
- **File**: `notebooks/02_data_preprocessing.ipynb`
- **Kernel**: `venv` (Python 3.13.7)

## Preprocessing Steps

### Step 1: Remove Error Values (-9999)
- **Rows with -9999**: 1 row
- **Action**: Dropped the row
- **Result**: 100,000 → 99,999 rows

### Step 2: Handle Missing Values
- **Missing values found**: 9 total (alpha:1, delta:2, run_ID:6)
- **Action**: Dropped all rows with any missing values (0.009% of data)
- **Result**: 99,999 → 99,990 rows

### Step 3: Fix Data Types
- **Columns converted**:
  - `alpha`: object → float64
  - `run_ID`: object → float64
- **Issues encountered**: 1 new NaN in each column during conversion
- **Action**: Dropped these 2 rows
- **Result**: 99,990 → 99,988 rows

### Step 4: Check Duplicates
- **Duplicates found**: 0
- **Dataset now clean**: 99,988 rows, no missing values, no duplicates

### Step 5: Feature Engineering - Color Indices
Created four color indices:
```python
df_clean['u-g'] = UV_filter - green_filter
df_clean['g-r'] = green_filter - red_filter  
df_clean['r-i'] = red_filter - near_IR_filter
df_clean['i-z'] = near_IR_filter - IR_filter
```

#### Color Indices Statistics

| Index | Mean  | Std   | Min     | Max    |
|-------|-------|-------|---------|--------|
| u-g   | 1.449 | 1.179 | -12.748 | 18.625 |
| g-r   | 0.986 | 0.735 | -12.319 | 14.315 |
| r-i   | 0.561 | 0.502 | -14.649 | 12.206 |
| i-z   | 0.316 | 0.420 | -13.162 | 13.427 |

### Step 6: Correlation Analysis

#### Key Findings:

- Visible light filters show strong positive correlations (0.93-0.97)
- Color indices show weak negative correlations with redshift
- Redshift shows positive correlation with magnitude filters (farther objects = fainter = higher magnitude numbers)

#### Correlations with Redshift:

| Feature        | Correlation |
|----------------|-------------|
| IR_filter      | +0.501      |
| near_IR_filter | +0.492      |
| red_filter     | +0.433      |
| green_filter   | +0.319      |
| UV_filter      | +0.167      |
| i-z            | -0.046      |
| r-i            | -0.124      |
| g-r            | -0.209      |
| u-g            | -0.233      |

### Step 7: Prepare for Modeling

#### Feature Selection (10 features):

```python
['UV_filter', 'green_filter', 'red_filter', 'near_IR_filter', 
 'IR_filter', 'red_shift', 'u-g', 'g-r', 'r-i', 'i-z']
```

#### Target Encoding:

- STAR → 0
- GALAXY → 1
- QSO → 2

#### Train-Validation-Test Split (70-15-15):

- Training: 69,991 rows (70.0%)
- Validation: 14,999 rows (15.0%)
- Test: 14,998 rows (15.0%)

#### Feature Scaling:

- Method: StandardScaler (fit on training only)
- All features now have mean=0, std=1

### Step 8: Save Preprocessed Data

Files saved in `models/` directory:

- `scaler.pkl`: Fitted StandardScaler
- `label_encoder.pkl`: LabelEncoder for classes
- `feature_names.pkl`: List of feature names
- `X_train.pkl`, `X_val.pkl`, `X_test.pkl`: Scaled features
- `y_train.pkl`, `y_val.pkl`, `y_test.pkl`: Encoded targets

## Final Dataset Summary

- Clean rows: 99,988 (99.988% of original)
- Features: 10 (5 magnitudes + redshift + 4 color indices)
- Target: 3 classes (STAR, GALAXY, QSO)

