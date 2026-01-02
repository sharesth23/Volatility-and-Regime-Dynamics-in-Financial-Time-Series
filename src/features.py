"""
Feature engineering for volatility and regime models.
"""

import pandas as pd
import numpy as np


def realized_volatility(returns, window=21):
    return returns.rolling(window).std()