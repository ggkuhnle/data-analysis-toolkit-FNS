#!/usr/bin/env python3

import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(11088)

# 🔧 Set sample size here
sample_size = 1000  # Change this to generate more or fewer records

# Possible categories
sexes = ["Male", "Female"]
smoking_statuses = ["Smoker", "Non-smoker"]
groups = ["Control", "Hipponol"]

# Generate synthetic data
data = []
for i in range(1, sample_size + 1):
    age = np.random.randint(40, 71)  # Age between 40 and 70
    sex = np.random.choice(sexes)
    smoking = np.random.choice(smoking_statuses)
    group = np.random.choice(groups)

    # Baseline blood pressure
    sbp_base = np.random.normal(135, 15)
    dbp_base = np.random.normal(85, 10)

    # Follow-up BP with a mild expected treatment effect
    sbp_follow = sbp_base + np.random.normal(-5 if group == "Hipponol" else 3, 10)
    dbp_follow = dbp_base + np.random.normal(-3 if group == "Hipponol" else 2, 8)

    # Generate raw time-to-event
    scale = 10 if group == "Hipponol" else 5  # More gradual decay for control
    raw_time = np.random.exponential(scale=scale)
    time_to_event = round(min(raw_time, 24.0), 1)

    # Apply censoring (40% chance) or if max time reached
    if np.random.rand() < 0.4 or time_to_event == 24.0:
        survival = 0  # Censored
    else:
        survival = 1  # Event occurred

    data.append([
        i, age, sex, smoking, group,
        round(sbp_base, 1), round(dbp_base, 1),
        round(sbp_follow, 1), round(dbp_follow, 1),
        survival, time_to_event
    ])

# Column names
columns = ["ID", "Age", "Sex", "SmokingStatus", "Group",
           "Baseline_SBP", "Baseline_DBP", "Followup_SBP", "Followup_DBP",
           "Survival", "Time_to_Event"]

# Create DataFrame and export
df = pd.DataFrame(data, columns=columns)
df.to_csv("../data/hipponol_trial_data.csv", index=False)

print(f"✅ Created 'hipponol_trial_data.csv' with {sample_size} entries.")
