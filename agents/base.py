import numpy as np

class MarketAgent:
    def __init__(self, name, risk_aversion, entropy_sensitivity):
        self.name = name
        self.risk_aversion = risk_aversion
        self.entropy_sensitivity = entropy_sensitivity
        self.position = 0.0

    def utility(self, expected_return, volatility, entropy):
        return (
            expected_return
            - self.risk_aversion * volatility
            - self.entropy_sensitivity * entropy
        )

    def act(self, market_state):
        raise NotImplementedError
