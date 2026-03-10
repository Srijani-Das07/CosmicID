# Phase 1: Data Acquisition - SDSS Dataset

## Data Source
- **Dataset**: Stellar Classification Dataset
- **Source**: Kaggle (Sonali Jindal)
- **URL**: https://www.kaggle.com/datasets/jsonali2003/stellar-classification-dataset

## Dataset Description
- **Size**: 100,000 observations
- **Source survey**: Sloan Digital Sky Survey (SDSS DR18) Data Release 18
- **File format**: CSV
- **File size**: ~13.3 MB
- **File name**: `sdss_stellar_classification.csv`

## Columns Description

| Column Name | Description | Data Type |
|-------------|-------------|-----------|
| obj_ID | Object identifier | float64 |
| alpha | Right Ascension (degrees) | object → float64 |
| delta | Declination (degrees) | float64 |
| UV_filter | u-band magnitude | float64 |
| green_filter | g-band magnitude | float64 |
| red_filter | r-band magnitude | float64 |
| near_IR_filter | i-band magnitude | float64 |
| IR_filter | z-band magnitude | float64 |
| run_ID | Run number | object → float64 |
| rerun_ID | Rerun number | int64 |
| cam_col | Camera column | int64 |
| field_ID | Field number | int64 |
| spec_obj_ID | Spectroscopic object ID | float64 |
| red_shift | Redshift value | float64 |
| plate_ID | Plate number | int64 |
| MJD | Modified Julian Date | int64 |
| fiber_ID | Fiber ID | int64 |
| class | Object class (STAR/GALAXY/QSO) | str |

## Data Storage
- **Raw data location**: `data/raw/sdss_stellar_classification.csv`
- **Data integrity**: Original file preserved, never modified directly

## Initial Observations
- Dataset contains all three classes needed for classification
- Redshift column present 
- Five photometric bands available (u,g,r,i,z)
- Some columns have string representations of numbers (need conversion)

