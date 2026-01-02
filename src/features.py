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

def volatility_features(returns):
    """
    Full feature set for volatility forecasting.
    """
    features = pd.DataFrame(index=returns.index)

    features["rv_5"] = realized_volatility(returns, 5)
    features["rv_21"] = realized_volatility(returns, 21)
    features["rv_63"] = realized_volatility(returns, 63)

    lagged = lagged_features(returns)
    features = pd.concat([features, lagged], axis=1)

    return features.dropna()
