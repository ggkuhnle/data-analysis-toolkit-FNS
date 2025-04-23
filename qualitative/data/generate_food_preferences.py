#!/usr/bin/env python3

import random
random.seed(42)
hippos = [f'H{i}' for i in range(1, 51)]
preferences = [
    'I enjoy crunchy carrots for their sweetness.',
    'Grass is acceptable, but fruit is preferred.',
    'More variety needed—vegetables are dull.',
    'Fruit smoothies are my favourite.',
    'Carrots and greens keep me strong.',
    'Prefer juicy fruits over grasses.',
    'Vegetables need more flavour.',
    'Love the crunch of fresh carrots.',
    'Fruit is the best part of my diet.',
    'Mixed greens are fine, but fruit wins.'
]
with open('food_preferences.txt', 'w') as f:
    for h in hippos:
        pref = random.choice(preferences)
        f.write(f'Hippo {h}: {pref}\n')
