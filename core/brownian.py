import numpy as np

def brownian_increment(dt=1.0):
    return np.random.normal(0, np.sqrt(dt))
