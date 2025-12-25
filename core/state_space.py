import numpy as np
import pandas as pd

class MarketStateSpace:
    def __init__(self, prices: pd.Series):
        self.prices = prices
        self.returns = self._compute_returns()
        self.volatility = self._compute_volatility()

    def _compute_returns(self):
        return np.log(self.prices / self.prices.shift(1)).dropna()

    def _compute_volatility(self, window=20):
        return self.returns.rolling(window).std()

    def get_state_vector(self):
        df = pd.DataFrame({
            "returns": self.returns,
            "volatility": self.volatility
        }).dropna()
        return df
