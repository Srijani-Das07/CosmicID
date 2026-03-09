# Phase 2: Data Loading & Initial Exploration

## Notebook
- **File**: `notebooks/01_data_loading.ipynb`
- **Kernel**: `venv` (Python 3.13.7)

## Key Findings

### 1. Dataset Shape
- **Rows**: 100,000
- **Columns**: 18

### 2. Class Distribution
| Class | Count | Percentage |
|-------|-------|------------|
| GALAXY | 59,445 | 59.4% |
| STAR | 21,594 | 21.6% |
| QSO | 18,961 | 19.0% |

*Galaxies most common, Quasars least common*

### 3. Missing Values (Initial)
| Column | Missing Count |
|--------|---------------|
| alpha | 1 |
| delta | 2 |
| run_ID | 6 |
| *Others* | 0 |

### 4. Data Quality Issues Identified

#### Error Values
- `UV_filter`: 1 row with -9999 (invalid magnitude)
- `green_filter`: 1 row with -9999
- `IR_filter`: 1 row with -9999

#### Data Type Issues
- `alpha`: stored as object (should be float)
- `run_ID`: stored as object (should be int)

### 5. Redshift Statistics
- **Min**: -0.009971 (one negative value - likely error)
- **Max**: 7.011245 (quasars up to z=7)
- **Mean**: 0.576 (matches galaxy range)
- **Distribution**: stars near 0, galaxies 0.1-0.6, quasars 1-7

### 6. Magnitude Statistics
- **Ranges**: Approximately 9-33 across filters
- **Error values**: -9999 present in three filters
- **Outliers**: Some extreme values need investigation

