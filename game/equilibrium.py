import numpy as np

def equilibrium_stress(payoffs):
    dispersion = np.std(payoffs)
    return dispersion  # high dispersion = unstable equilibrium
