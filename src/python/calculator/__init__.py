# src/python/calculator/__init__.py
"""
Calculator Package
==================

A hybrid Python and C calculator that can be used as a library or a CLI tool.

This package exposes a simple `Calculator` class with static methods
for performing arithmetic operations.
"""

# Import the Calculator class to make it directly accessible when the package is imported.
# e.g., from calculator import Calculator
from .calculator import Calculator

# Define package-level metadata.
__version__ = "1.0.0"
__author__ = "Ali_AND_Anas"

# __all__ controls what 'from calculator import *' imports.
__all__ = ["Calculator"]
