#!/usr/bin/env python3
# create_epi_data.py
# Script to simulate an epidemiological dataset for nutrition science studies

# Import required libraries
import numpy as np
import pandas as pd
import scipy  # Import scipy to check its version
from scipy.stats import norm, expon

# Check dependency versions to avoid compatibility issues
def check_dependencies():
    required_numpy = "1.26.4"
    required_scipy = "1.12.0"
    installed_numpy = np.__version__
    installed_scipy = scipy.__version__  # Corrected: Use scipy.__version__ instead of pd.__version__

    if installed_numpy != required_numpy:
        print(f"Warning: NumPy version {installed_numpy} installed. Expected {required_numpy}.")
        print("Please run: pip install numpy==1.26.4")
    if installed_scipy != required_scipy:
        print(f"Warning: SciPy version {installed_scipy} installed. Expected {required_scipy}.")
        print("Please run: pip install scipy==1.12.0")

check_dependencies()

# Set random seed for reproducibility
np.random.seed(11088)

# Sample size
n = 25000

# Simulate baseline data
try:
    data = pd.DataFrame({
        'ID': range(1, n + 1),
        'Age': np.random.randint(45, 81, size=n),  # Age 45-80
        'Sex': np.random.choice(['M', 'F'], size=n, p=[0.5, 0.5]),  # 50% Male, 50% Female
        'Smoking': np.random.choice(['Yes', 'No'], size=n, p=[0.3, 0.7]),  # 30% smokers
        'Physical_Activity': np.random.choice(['Low', 'Medium', 'High'], size=n, p=[0.4, 0.4, 0.2]),  # Activity levels
        'Social_Class': np.random.choice(['A', 'B', 'C1', 'C2', 'D', 'E'], size=n, p=[0.1, 0.15, 0.25, 0.25, 0.15, 0.1]),  # UK social class
        'BMI_Baseline': norm.rvs(loc=27, scale=4, size=n),  # Baseline BMI, mean=27, SD=4
        'BP_Baseline': norm.rvs(loc=130, scale=15, size=n),  # Baseline systolic BP, mean=130, SD=15
        'Sugar_Intake': norm.rvs(loc=50, scale=10, size=n),  # Sugar intake (g/day), mean=50, SD=10
        'SFA_Intake': norm.rvs(loc=30, scale=8, size=n)  # Saturated fat intake (g/day), mean=30, SD=8
    })

    # Simulate follow-up data (2, 4, 6 years)
    # BMI increases with sugar intake; BP changes randomly
    for year in [2, 4, 6]:
        bmi_effect = 0.02 * data['Sugar_Intake']  # Sugar intake increases BMI over time
        data[f'BMI_Year{year}'] = data['BMI_Baseline'] + bmi_effect + norm.rvs(loc=0, scale=1, size=n)
        data[f'BP_Year{year}'] = data['BP_Baseline'] + norm.rvs(loc=0, scale=5, size=n)

    # Simulate CVD incidence (survival endpoint)
    # SFA intake increases CVD risk; other factors also contribute
    hazard = 0.0001 + 0.00005 * data['SFA_Intake'] + 0.00002 * data['Age'] + 0.00003 * (data['BP_Baseline'] - 130)
    time_to_cvd = expon.rvs(scale=1/hazard)
    data['CVD_Incidence'] = (time_to_cvd <= 6).astype(int)  # CVD within 6 years
    data['Time_to_CVD'] = np.minimum(time_to_cvd, 6)  # Censor at 6 years

    # Introduce random missing data (5-10%)
    for col in data.columns:
        if col != 'ID':
            mask = np.random.choice([True, False], size=n, p=[0.08, 0.92])  # ~8% missing
            data.loc[mask, col] = np.nan

    # Save the dataset
    data.to_csv('epidemiological_study.csv', index=False)
    print("Dataset simulated and saved as 'epidemiological_study.csv'")

except Exception as e:
    print(f"An error occurred while generating the dataset: {e}")
