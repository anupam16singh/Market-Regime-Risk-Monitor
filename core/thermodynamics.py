import numpy as np

class MarketThermodynamics:
    def __init__(self, energy, entropy, temperature):
        self.energy = energy
        self.entropy = entropy
        self.temperature = temperature

    def free_energy(self):
        return self.energy - self.temperature * self.entropy

    def entropy_production_rate(self):
        return np.gradient(self.entropy)
