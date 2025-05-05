#!/usr/bin/env python3

# Script to generate a synthetic metabolomics dataset for use in 5 multivariate analysis notebooks
# Author: Grok (assisting with learning-focused comments)
# Date: 26 April 2025

# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Set random seed for reproducibility
np.random.seed(11088)

# Define dataset parameters
n_samples        = 1000 # Number of samples (e.g., patients)
n_metabolites    =  200 # Number of metabolites (features)
n_latent_factors =   9  # Number of latent factors to create correlated metabolite groups
prop_diseased    = 0.2  # Proportion of samples in diseased class

# Step 1: Generate latent factors to create correlated metabolites
# Each factor represents a biological pathway influencing a subset of metabolites
latent_factors = np.random.randn(n_samples, n_latent_factors)  # Random latent scores

# Step 2: Create loadings to map latent factors to metabolites
# Loadings define which metabolites are influenced by each factor
loadings = np.zeros((n_metabolites, n_latent_factors))
for i in range(n_metabolites):
    # Each metabolite is influenced by 1-2 factors (sparse structure)
    active_factors = np.random.choice(n_latent_factors, size=np.random.randint(1, 3), replace=False)
    loadings[i, active_factors] = np.random.uniform(0.5, 1.5, size=len(active_factors))

# Step 3: Generate base metabolite data (without noise)
base_data = latent_factors @ loadings.T  # Matrix multiplication: samples x metabolites

# Step 4: Add class-specific effects (make some metabolites discriminative)
labels = np.random.choice([0, 1], size=n_samples, p=[1 - prop_diseased, prop_diseased])
discriminative_metabolites = np.random.choice(n_metabolites, size=10, replace=False)  # 10 discriminative metabolites
for met in discriminative_metabolites:
    # Diseased samples (label=1) have higher values for these metabolites
    base_data[labels == 1, met] += np.random.uniform(1, 2)  # Shift mean for diseased

# Step 5: Add noise to mimic biological/technical variability
noise = np.random.normal(0, 0.3, size=(n_samples, n_metabolites))
data = base_data + noise

# Step 6: Ensure positive values (metabolite concentrations are non-negative)
data = np.abs(data)  # Take absolute value
data = StandardScaler().fit_transform(data)  # Standardize (mean=0, variance=1) for analysis

# Step 7: Generate continuous outcome (disease severity)
# Severity is correlated with discriminative metabolites and PC1
severity = (
    0.5 * np.mean(data[:, discriminative_metabolites], axis=1)  # Influence of discriminative metabolites
    + 0.3 * np.random.randn(n_samples)  # Random noise
)
severity = (severity - severity.mean()) / severity.std()  # Standardize severity

# Step 8: Create DataFrame
columns = [f'Metabolite_{i+1}' for i in range(n_metabolites)]  # Name metabolites
df = pd.DataFrame(data, columns=columns)
df['Label'] = labels  # Add binary labels (0=healthy, 1=diseased)
df['Severity'] = severity  # Add continuous severity score

# Step 9: Save dataset to CSV
df.to_csv('metabolomics_dataset.csv', index=False)
print("Dataset saved as 'metabolomics_dataset.csv'")

# Step 10: Create metadata file
metadata = """
Synthetic Metabolomics Dataset
============================
- Samples: 1000
- Features: 200 metabolites (standardized, continuous)
- Label: Binary (0=healthy, 1=diseased, ~20% diseased)
- Severity: Continuous disease severity score
- Structure: Metabolites are correlated via 9 latent factors (biological pathways).
- Discriminative Metabolites: 10 metabolites have higher values in diseased samples.
- Usage: Suitable for PCA, PLS-DA, Bayesian models, Random Forests, and regression.
- Generated: 26 April 2025
- Random Seed: 11088
"""
with open('../data/metabolomics_dataset_metadata.txt', 'w') as f:
    f.write(metadata)
print("Metadata saved as 'metabolomics_dataset_metadata.txt'")
