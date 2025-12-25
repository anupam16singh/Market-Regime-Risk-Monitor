from agents.base import MarketAgent
import numpy as np

class RetailAgent(MarketAgent):
    def act(self, market_state):
        if market_state["volatility"] > market_state["vol_threshold"]:
            self.position += np.random.choice([-1, 1]) * 0.2
        return self.position
