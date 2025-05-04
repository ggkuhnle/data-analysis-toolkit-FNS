"""Thin PyMC/ArviZ model builders."""
import pymc as pm
import arviz as az

def bayesian_logistic(X, y, **model_kwargs):
    with pm.Model() as model:
        # define priors, likelihood…
        trace = pm.sample(**model_kwargs, return_inferencedata=True)
    return trace

