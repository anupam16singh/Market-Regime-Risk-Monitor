import numpy as np

class MarketEntropy:
    def __init__(self, returns):
        self.returns = np.asarray(returns)

    def gaussian_entropy(self, data=None):
        """
        Differential entropy of a Gaussian distribution.
        """
        if data is None:
            data = self.returns

        sigma = np.std(data)
        if sigma <= 0:
            return 0.0

        return 0.5 * np.log(2 * np.pi * np.e * sigma**2)

    def rolling_entropy(self, window=100):
        ent = []

        for i in range(window, len(self.returns)):
            window_returns = self.returns[i - window : i]
            ent.append(self.gaussian_entropy(window_returns))

        return np.array(ent)
