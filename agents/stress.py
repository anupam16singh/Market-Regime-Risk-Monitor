import numpy as np

class StructuralStress:
    def __init__(self, agent_payoffs):
        self.agent_payoffs = agent_payoffs

    def stress_index(self):
        return np.var(self.agent_payoffs)

    def stress_level(self):
        s = self.stress_index()
        if s < 0.2:
            return "LOW"
        elif s < 0.5:
            return "MEDIUM"
        return "HIGH"
