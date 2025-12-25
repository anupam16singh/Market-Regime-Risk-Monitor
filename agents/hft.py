from agents.base import MarketAgent
import numpy as np

class HFTAgent(MarketAgent):
    def act(self, market_state):
        self.position += np.sign(
            market_state["order_imbalance"]
        ) * 0.05
        return self.position
