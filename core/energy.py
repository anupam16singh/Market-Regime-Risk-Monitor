class MarketEnergy:
    def __init__(self, volatility, liquidity=1.0):
        self.volatility = volatility
        self.liquidity = liquidity

    def energy(self):
        return self.liquidity / (self.volatility + 1e-9)

    def free_energy(self, entropy, temperature=1.0):
        return self.energy() - temperature * entropy
