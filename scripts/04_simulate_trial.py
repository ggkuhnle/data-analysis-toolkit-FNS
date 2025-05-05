#!/usr/bin/env python3

import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Simulate data
n_participants = 100
data = {
    'participant_id': range(1, n_participants + 1),
    'age': np.random.normal(loc=40, scale=10, size=n_participants),
    'bmi': np.random.normal(loc=27, scale=4, size=n_participants),
    'group': np.random.choice([0, 1], size=n_participants, p=[0.5, 0.5]),
}
data['outcome'] = np.where(
    data['group'] == 0,
    np.random.normal(loc=0, scale=2, size=n_participants),
    np.random.normal(loc=1, scale=2, size=n_participants)
)

# Create DataFrame and save
df = pd.DataFrame(data)
df.to_csv('../data/simulated_trial.csv', index=False)
print('Dataset saved as data/simulated_trial.csv')
