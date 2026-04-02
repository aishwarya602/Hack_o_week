# Predictive Maintenance using Sensor Data (Kaggle Dataset)

## Description

This project focuses on predicting machine failures using sensor data from a dataset obtained via Kaggle. It applies feature engineering techniques to derive a proximity-like stress index, followed by training a machine learning model to classify potential failures.

---

## Objectives
- Analyze industrial sensor data
- Engineer meaningful features (stress/proximity index)
- Train a machine learning model for failure prediction
- Evaluate model performance using standard metrics

## Dataset
- Source: Kaggle
- Dataset: AI4I 2020 Predictive Maintenance Dataset
- Features used:
    - Air Temperature
    - Process Temperature
    - Torque
    - Tool Wear
- Target:
Machine Failure (0 = No Failure, 1 = Failure)

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn

## Workflow
1. Data Loading
    - Import dataset using Pandas
2. Data Preprocessing
    - Clean and inspect data
    - Handle missing values
    - Normalize features
3. Feature Engineering
    - Created Stress Index using weighted combination of sensor values
    - Normalized stress index
    - Generated binary High-Risk feature
4. Model Training
    - Used Random Forest Classifier
    - Split dataset into training and testing sets
5. Evaluation
    - Accuracy score
    - Classification report
    - Feature importance analysis

## Output
🔹 Model Performance
        - Accuracy score
        - Precision, Recall, F1-score
🔹 Visualization
        - Stress index trend
        - Feature importance graph

## Project Structure
├── data/
│   └── ai4i2020.csv
├── src/
│   └── model.py
├── notebook/
│   └── analysis.ipynb
├── README.md

## How to Run
- pip install pandas numpy matplotlib scikit-learn
- python model.py

## Future Improvements
- Try Logistic Regression / XGBoost
- Apply time-series models (LSTM)
- Build real-time monitoring dashboard
- Integrate with IoT systems

## Applications
- Industrial predictive maintenance
- Smart manufacturing systems
- Equipment health monitoring
- Failure prevention systems