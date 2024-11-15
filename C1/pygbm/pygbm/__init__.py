"""
PyGBM: A Python package for simulating Geometric Brownian Motion

This package provides tools for simulating and analyzing Geometric Brownian Motion.
"""

__author__ = "Prithvi Singh"
__version__= "0.1.0"

from .gbm import GBM
import numpy as np

__all__= [
    "GBM",
    "simulate_paths",
]

