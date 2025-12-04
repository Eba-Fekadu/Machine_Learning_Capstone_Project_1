# AI Coding Agent Instructions - ML Capstone Project

## Project Overview
This is a collaborative ML capstone project applying machine learning to solar irradiance and weather data from three African locations (Benin-Malanville, Sierra Leone-Bumbuna, Togo-Dapaong). The project spans from data preprocessing through model evaluation, with independent work through task 3, then collaborative model development with assigned leaders.

## Data Architecture
**Key datasets** (`data/` directory):
- `benin-malanville.csv`: ~525K records, solar irradiance (Benin location)
- `sierraleone-bumbuna.csv`: ~525K records, solar irradiance (Sierra Leone location)  
- `togo-dapaong_qc.csv`: ~525K records, solar irradiance (Togo location)

**Data schema** (identical across all files):
- **Irradiance**: GHI (Global Horizontal), DNI (Direct Normal), DHI (Diffuse Horizontal)
- **Module Performance**: ModA, ModB (Panel A & B power output)
- **Weather**: Tamb (Ambient temp), RH (Relative Humidity), WS (Wind Speed), WSgust, WSstdev
- **Wind direction**: WD, WDstdev; Atmospheric: BP (Barometric Pressure)
- **Maintenance**: Cleaning flag, Precipitation, TModA/TModB (Panel temperatures)
- **Quality**: Comments column for data notes

Timestamps are 1-minute resolution starting 2021-08-09 (Benin) and 2021-10-25 (Sierra Leone/Togo).

## Workflow & Development Phases
The project follows structured phases:
1. **Task 1-3** (Independent): Data preprocessing, EDA, feature engineering per developer
2. **Task 4+** (Collaborative): Model building with designated leader per ML algorithm
3. **Daily standups** ensure coordination across the three parallel data streams

## Development Structure

### Notebooks (`notebooks/`)
- `EDA.ipynb`: Primary exploratory data analysis notebook (empty/pending)
- Expected additions: model-specific notebooks for leader-assigned model development
- **Pattern**: Use notebooks for analysis + visualization; scripts for reproducible pipelines

### Scripts (`scripts/`)
- `initial.py`: Template/initial setup script (currently empty)
- **Expected pattern**: Modular scripts for data loading, preprocessing, feature engineering
- **Convention**: Separate scripts by functional purpose (e.g., `preprocessing.py`, `feature_engineering.py`, `model_training.py`)

## Data Processing Conventions

### Handling Multi-Location Data
- Load all three datasets independently initially (EDA phase)
- For aggregated models: concatenate with location identifier column
- Consider location-specific modeling due to different climates (tropical vs equatorial)

### Time Series Considerations
- Timestamps are 1-minute granular; expect resampling to hourly/daily for most ML models
- Handle missing/negative irradiance values (-1.2, -0.2 represent night/invalid measurements)
- Check for gaps in timestamps during data quality checks

### Missing Value Strategy
- Comments column often empty; treat as metadata, not predictor
- Monitor ModA/ModB values (often 0 at night); apply domain-aware imputation
- Check BP (pressure) and RH (humidity) for realistic ranges by location

## Modeling Workflow

### Multi-Model Leadership Structure
- Each team member leads ONE ML model implementation
- Others contribute code review and optimization
- Script organization: `scripts/model_<name>.py` (e.g., `model_lstm.py`, `model_xgboost.py`)

### Feature Engineering Targets
Common ML targets (irradiance forecasting):
- **Regression**: Predict next-period GHI/DNI/DHI values
- **Classification**: Cloud presence detection (GHI thresholding)
- Temporal features: hour-of-day, day-of-week, seasonal cycles
- Interaction features: temp-humidity, wind-pressure relationships

### Model Evaluation
- Use train/test split respecting temporal ordering (no data leakage across dates)
- Report: RMSE, MAE, R² for regression; precision/recall for classification
- Document location-specific performance differences
- Store results in consistent format for comparison across models

## Critical Implementation Notes

### Dependencies & Environment
- Primary: pandas, scikit-learn, numpy for classical ML
- Time series: Consider statsmodels, Prophet for seasonal decomposition
- Deep learning (if used): TensorFlow/PyTorch for LSTM/neural approaches
- Visualization: matplotlib, seaborn for notebooks

### Code Collaboration Patterns
- Branch naming: `feature/<task-name>` or `model/<leader-name>/<model-type>`
- PR discipline: Describe task number, location-specific findings, model assumptions
- Review for: data leakage, temporal correctness, location generalizability

### Common Pitfalls to Avoid
1. **Time leakage**: Don't use future values in feature windows
2. **Location bias**: Test each location separately before aggregation
3. **Negative/zero values**: GHI/DNI at night are -1.x by design; don't treat as outliers
4. **Scaling**: Different locations have different climate ranges; normalize per-location
5. **Data imbalance**: Night hours dominate (~12 hours); stratify train/test by daylight

## File References
- Project root: All main documents and `.git/`
- **Data loading template**: Establish in first version of `scripts/initial.py`
- **EDA reference**: Build in `notebooks/EDA.ipynb` once structure settled
- **Reproducibility**: All model scripts should load data from `data/` relative paths

## Team Coordination
- Sync daily on preprocessing findings, especially anomalies per location
- Document model assumptions and location-specific parameters
- Share feature engineering discoveries (what features work across locations vs. location-specific)
- Final deliverable: Comparison table of all models across the three locations
