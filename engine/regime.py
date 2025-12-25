import numpy as np

def classify_regime(entropy, volatility):
    if entropy < np.percentile(entropy, 30):
        return "ORDERED"
    elif entropy < np.percentile(entropy, 70):
        return "TRANSITION"
    else:
        return "DISORDERED"
