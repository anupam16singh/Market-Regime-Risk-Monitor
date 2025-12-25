import numpy as np

def instability_probability(entropy_rate, threshold=0.01):
    spikes = entropy_rate > threshold
    return np.mean(spikes)
