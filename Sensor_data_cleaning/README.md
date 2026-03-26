#  IoT Sensor Data Cleaning using Pandas

##  Project Overview

This project focuses on cleaning and preprocessing raw IoT sensor data using Python. Sensor data often contains missing values, noise, and outliers, which can negatively impact analysis and machine learning models.

The goal of this project is to transform raw sensor readings into a clean and structured dataset ready for further analysis or ML tasks.

---

##  Objectives

* Load and explore IoT sensor dataset
* Handle missing values efficiently
* Detect and remove outliers
* Smooth noisy sensor readings
* Normalize data for machine learning
* Export a cleaned dataset

---

##  Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn

---

##  Project Structure

```
project/
│── sensor_data_cleaning.py
│── iot_sensor_data.csv
│── cleaned_iot_sensor_data.csv
│── README.md
```

---

##  Steps Performed

### 1. Data Loading

* Loaded CSV dataset using Pandas
* Displayed initial rows and dataset structure

### 2. Data Exploration

* Checked shape, columns, and summary statistics
* Identified missing values

### 3. Handling Missing Values

* Used forward fill (`ffill`) and backward fill (`bfill`)
* Ensured no null values remain

### 4. Outlier Detection & Removal

* Applied IQR (Interquartile Range) method
* Removed extreme values beyond acceptable range
* Optional: Used Z-score method for additional filtering

### 5. Data Smoothing

* Applied rolling mean to reduce noise in sensor readings

### 6. Normalization

* Scaled numerical features using MinMaxScaler
* Prepared data for machine learning models

### 7. Data Export

* Saved cleaned dataset as:

  ```
  cleaned_iot_sensor_data.csv
  ```

---

## Example Features in Dataset

* `timestamp` → Time of reading
* `temperature` → Sensor temperature values
* `humidity` → Humidity readings
* `distance` → Proximity sensor readings

---

##  How to Run

1. Clone the repository:

```
git clone https://github.com/your-username/iot-data-cleaning.git
```

2. Navigate to the project folder:

```
cd iot-data-cleaning
```

3. Install dependencies:

```
pip install pandas numpy matplotlib scikit-learn
```

4. Run the script:

```
python iot_data_cleaning.py
```

---

##  Output

* Cleaned dataset without missing values
* Reduced noise and outliers
* Normalized data ready for ML models

---

## Future Improvements

* Real-time sensor data processing
* Anomaly detection using machine learning
* Data visualization dashboard
* Integration with IoT devices

---


