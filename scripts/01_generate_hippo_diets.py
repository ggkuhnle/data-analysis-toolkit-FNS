#!/usr/bin/env python3

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
np.random.seed(42)
hippos = [f'H{i}' for i in range(1, 51)]
start_date = datetime(2024, 1, 1)
data = []
for i, h in enumerate(hippos):
    calories = np.random.normal(2450, 150)
    protein = np.random.normal(78, 5) if np.random.rand() > 0.1 else np.nan
    date = (start_date + timedelta(days=i)).strftime('%Y-%m-%d')
    data.append([h, round(calories), round(protein, 1) if not np.isnan(protein) else np.nan, date])
df = pd.DataFrame(data, columns=['ID', 'Calories', 'Protein', 'Date'])
df.to_csv('../data/hippo_diets.csv', index=False)
