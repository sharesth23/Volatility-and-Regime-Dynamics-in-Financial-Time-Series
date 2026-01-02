import numpy as np


def annualize_vol(vol, freq=252):
    return vol * np.sqrt(freq)
