#!/usr/bin/env python3

import pandas as pd
import numpy as np
np.random.seed(42)
data = []
for i in range(1, 201):
    pid = f'P{i}'
    if i % 2 == 1:
        group = 'Control'
        vit_d = np.random.normal(10, 0.5)
        time = 0
        outcome = 'Normal'
    else:
        group = 'Treatment'
        vit_d = np.random.normal(15.5, 0.7)
        time = 1
        outcome = 'Improved'
    data.append([pid, group, round(vit_d, 1), time, outcome])
df = pd.DataFrame(data, columns=['ID', 'Group', 'Vitamin_D', 'Time', 'Outcome'])
df.to_csv('../data/vitamin_trial.csv', index=False)
