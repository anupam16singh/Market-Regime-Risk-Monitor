from agents.base import MarketAgent
import numpy as np

class InstitutionalAgent(MarketAgent):
    def act(self, market_state):
        if market_state["entropy"] > market_state["entropy_threshold"]:
            self.position *= 0.8  # de-risk
        else:
            self.position += 0.1
        return self.position
