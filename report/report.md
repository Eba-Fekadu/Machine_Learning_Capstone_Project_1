# Optimizing Ethiopia's Solar Future: A Data-Driven Strategy for MoonLight Energy Solutions

## 1. Introduction: The Pulse of Renewable Energy
As Ethiopia moves towards its ambitious National Electrification Program, the need for precision in solar energy deployment has never been higher. At **MoonLight Energy Solutions**, we are committed to enhancing operational efficiency and sustainability by identifying high-potential regions for solar farm investments.

This project focuses on predicting **Global Horizontal Irradiance (GHI)** a critical metric for measuring solar radiation—using meteorological data from Benin, Sierra Leone, and Togo. By developing high-accuracy regression models, we aim to provide a scalable blueprint for site selection in Ethiopia, particularly across sun-rich regions like **Afar, Oromia, and Amhara**.

## 2. Dataset Overview: Capturing the Sun's Signal
Our analysis is powered by a robust dataset of environmental measurements, including:
- **Solar Irradiance**: GHI, DNI (Direct Normal Irradiance), and DHI (Diffuse Horizontal Irradiance).
- **Surface Measurements**: Module temperatures (TModA, TModB) and sensor readings (ModA, ModB).
- **Atmospheric Conditions**: Ambient Temperature (Tamb), Relative Humidity (RH), Wind Speed (WS, WSgust, WSstdev), and Barometric Pressure (BP).
- **Environmental Events**: Cleaning occurrences and Precipitation levels.

## 3. Exploratory Data Analysis (EDA): Uncovering Patterns
Before modeling, we performed a deep dive into the data to ensure quality and uncover relationships.

### Data Engineering & Cleaning
- **Missing Values**: The 'Comments' column was entirely null and removed. Other features were complete, showing high data integrity.
- **Outlier Detection**: Using **Isolation Forest**, we identified and pruned anomalous readings (approximately 2% of the dataset) to prevent noise from distorting our predictions.
- **Distribution Analysis**: GHI and DNI distributions confirmed that these regions experience intense peak radiation, ideal for large-scale solar arrays.

### Key EDA Insights
- **Diurnal Trends**: Time-series plots clearly showed consistent peak radiation periods, allowing us to accurately predict harvesting windows.
- **Correlations**: We found extremely strong linear relationships between GHI and both **DNI** and **DHI**. Additionally, **Module Temperature** showed a strong positive correlation with solar intensity.
- **Wind Dynamics**: Correlation analysis indicated that wind direction variability (WDstdev) was less relevant for GHI prediction compared to wind speed and gustiness.

## 4. Feature Engineering: Preparing for Prediction
To maximize model performance, we transformed the raw data into machine-learnable features:
1.  **Temporal Features**: Extracted `Hour`, `Month`, and `DayOfYear` from the `Timestamp` to capture seasonal and daily cycles.
2.  **Derived Metrics**: Created a `WSgust_ratio` to capture wind variability and a `HeatIndex` to understand the combined effect of temperature and humidity.
3.  **Scaling**: Applied `StandardScaler` to normalize numeric features, ensuring models like KNN and Linear Regression wouldn't be biased by feature magnitudes.

## 5. Regression Modeling: Picking the Winner
We experimented with various train/validation/test split ratios (0.8/0.1/0.1 proved robust) and a stack of sophisticated algorithms.

### Model Performance Comparison
Each model was evaluated using Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and R-squared (R²).

| Model | MSE | RMSE | R² Score |
| :--- | :--- | :--- | :--- |
| Linear Regression | 0.005167 | 0.071881 | 0.994475 |
| KNN | 0.003999 | 0.063235 | 0.995724 |
| Random Forest | 0.000276 | 0.016603 | 0.999705 |
| **XGBoost** | **0.000194** | **0.013926** | **0.999793** |
| LightGBM | 0.000342 | 0.018493 | 0.999634 |

### Interpretability & Insights
- **The Best Performer**: **XGBoost** emerged as the superior model, achieving an **R² score of 99.98%**. This level of accuracy ensures that MoonLight Energy Solutions can trust these forecasts for operational planning.
- **Key Predictors**: Feature importance plots from our Random Forest and XGBoost models confirmed that **Direct Normal Irradiance (DNI)** and **Module Temperature** are the most critical inputs for predicting GHI.

## 6. Recommendations: Powering Ethiopia
Based on the modeling results and high-GHI thresholds identified, we recommend the following strategic actions for MoonLight Energy Solutions in Ethiopia:

1.  **Prioritize the Afar Region**: Given the model's high sensitivity to DNI, the Afar region, with its consistently clear skies and high radiation levels, is the top priority for the next deployment phase.
2.  **Sensor Maintenance**: Since DNI and DHI are the strongest predictors, high-precision maintenance of pyrheliometers and pyranometers is mandatory to maintain forecast reliability.
3.  **Hybrid Cooling Systems**: The strong link between Module Temperature and GHI suggests that installing cooling mechanisms (e.g., passive heat sinks) in hot regions like **Oromia** could improve energy harvest efficiency during peak hours.

## 7. Conclusion
By merging advanced data science with renewable energy objectives, we have successfully developed a tool that can predict solar potential with near-perfect accuracy. These insights bring MoonLight Energy Solutions one step closer to optimizing solar farm deployment, directly contributing to Ethiopia’s goal of universal energy access and a greener future.
