#!/usr/bin/env python3

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
np.random.seed(42)
hippos = [f'H{i}' for i in range(1, 51)]
meals = ['Breakfast', 'Lunch', 'Dinner']
nutrients = ['Iron', 'Calcium', 'Protein', 'Vitamin_D']
start_date = datetime(2024, 1, 1)
data = []
for i in range(500):
    h = np.random.choice(hippos)
    meal = np.random.choice(meals)
    nutrient = np.random.choice(nutrients)
    if nutrient == 'Iron':
        amount = np.random.normal(2.5, 0.3)
    elif nutrient == 'Calcium':
        amount = np.random.normal(300, 30)
    elif nutrient == 'Protein':
        amount = np.random.normal(25, 3)
    else:
        amount = np.random.normal(11, 1)
    date = (start_date + timedelta(days=i % 90)).strftime('%Y-%m-%d')
    data.append([h, meal, nutrient, round(amount, 1), date])
df = pd.DataFrame(data, columns=['ID', 'Meal', 'Nutrient', 'Amount', 'Date'])
df.to_csv('large_food_log.csv', index=False)
