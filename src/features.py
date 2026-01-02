"""
Feature engineering for volatility and regime models.
"""

import pandas as pd
import numpy as np


def realized_volatility(returns, window=21):
    return returns.rolling(window).std()

def lagged_features(returns, lags=5):
    """
    Lagged absolute and squared returns.
    """
    df = pd.DataFrame(index=returns.index)

    for i in range(1, lags + 1):
        df[f"abs_ret_lag_{i}"] = returns.abs().shift(i)
        df[f"sq_ret_lag_{i}"] = returns.pow(2).shift(i)

    return df
