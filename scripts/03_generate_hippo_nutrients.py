#!/usr/bin/env python

import pandas as pd
import numpy as np

np.random.seed(42)
hippos = [f'H{i}' for i in range(1, 51)]
nutrients = ['Iron', 'Calcium', 'Vitamin_D']
years = [2024, 2025]
data = []
for h in hippos:
    for n in nutrients:
        for y in years:
            age = np.random.randint(20, 41)
            sex = np.random.choice(['M', 'F'])
            if n == 'Iron':
                value = np.random.normal(8, 0.5) if np.random.rand() > 0.1 else np.nan
            elif n == 'Calcium':
                value = np.random.normal(1150, 100) if np.random.rand() > 0.1 else np.nan
            else:
                value = np.random.normal(10.5, 1) if np.random.rand() > 0.1 else np.nan
            data.append([h, n, y, round(value, 1) if not np.isnan(value) else np.nan, age, sex])
df = pd.DataFrame(data, columns=['ID', 'Nutrient', 'Year', 'Value', 'Age', 'Sex'])
df.to_csv('../data/hippo_nutrients.csv', index=False)
