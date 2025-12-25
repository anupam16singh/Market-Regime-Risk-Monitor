import numpy as np

def build_features(entropy, entropy_rate, free_energy, stress):
    """
    Feature vector for ML observer.
    """
    return np.column_stack([
        entropy,
        entropy_rate,
        free_energy,
        stress
    ])
