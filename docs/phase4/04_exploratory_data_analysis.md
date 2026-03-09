# Phase 4: Exploratory Data Analysis (EDA)

## Notebook
- **File**: `notebooks/03_eda.ipynb`
- **Kernel**: `venv` (Python 3.13.7)

## Visualizations Created

### 1. Redshift Distribution
**Files**: 
- `visualizations/redshift_distribution.png`

**Key Insights**:
- **STAR**: Sharp peak near z≈0 (within our galaxy)
- **GALAXY**: Distributed in z=0.1-0.6 range (moderate distance)
- **QSO**: Spread across z=1-7 (extremely distant)
- Confirms redshift as the dominant discriminator

### 2. Magnitude Distributions
**File**: `visualizations/magnitude_boxplots.png`

**Key Insights**:
- All filters show overlapping ranges across classes
- Magnitude ranges: approximately 9-33 across all filters
- Magnitude alone cannot reliably distinguish classes
- Quasars show wider spread

### 3. Color-Magnitude Diagram
**File**: `visualizations/color_magnitude.png`

**Key Insights**:
- Scatter plot of u-g vs g-r shows partial clustering
- Some separation visible but considerable overlap
- Color indices reveal subtle class separations

### 4. Correlation Heatmap
**File**: `visualizations/correlation_heatmap.png`

**Key Insights**:
- Visible light filters show strong positive correlations (0.93-0.97) 
- Color indices show weak negative correlations with redshift
- Redshift shows positive correlation with magnitude filters (farther = fainter = higher magnitude)

**Correlations with Redshift**:
| Feature | Correlation |
|---------|-------------|
| IR_filter | +0.501 |
| near_IR_filter | +0.492 |
| red_filter | +0.433 |
| green_filter | +0.319 |
| UV_filter | +0.167 |
| i-z | -0.046 |
| r-i | -0.124 |
| g-r | -0.209 |
| u-g | -0.233 |

### 5. Quasar Variability Analysis
**File**: `visualizations/quasar_analysis.png`

**Key Insights**:
- Quasars show widest magnitude ranges across all filters
- Redshift distribution for QSO: z≈0.5 to 7.0
- Quasars exhibit high variability and extreme values
- Makes quasars the most challenging class for classification

### 6. Pairplot of Key Features
**File**: `visualizations/pairplot.png`

**Key Insights**:
- No single two-feature combination perfectly separates all classes
- Multi-dimensional space required for accurate classification

## Summary Statistics

1. REDSHIFT RANGES BY CLASS:
   STAR: min=-0.794, max=-0.783, mean=-0.789
   GALAXY: min=-0.802, max=1.934, mean=-0.212
   QSO: min=-0.788, max=8.779, mean=1.563

2. MAGNITUDE RANGES (showing overlap):
   UV_filter: -4.92 - 4.74
   green_filter: -4.98 - 5.38
   red_filter: -5.30 - 5.34
   near_IR_filter: -5.47 - 7.42
   IR_filter: -5.19 - 5.67

3. COLOR INDICES SUMMARY:
   u-g: mean=0.000, std=1.000
   g-r: mean=-0.000, std=1.000
   r-i: mean=0.000, std=1.000
   i-z: mean=0.000, std=1.000

4. CLASS DISTRIBUTION:
   GALAXY: 41604 (59.4%)
   STAR: 15115 (21.6%)
   QSO: 13272 (19.0%)


## Key Takeaways for Modeling

| Insight | Implication for Modeling |
|---------|-------------------------|
| Redshift is key discriminator | Must include redshift in all models |
| Magnitudes overlap | Cannot rely on single magnitude features |
| Color indices help | Include all 4 color indices |
| Quasars are challenging | Model needs to handle extreme values |
| Multi-dimensional needed | Use all 10 features, not just 2D combinations |

## Visualizations Saved
All plots are saved in the `visualizations/` folder.
