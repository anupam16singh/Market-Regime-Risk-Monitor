from agents.institutional import InstitutionalAgent
from agents.retail import RetailAgent
from agents.hft import HFTAgent
from game.payoff import payoff
from game.equilibrium import equilibrium_stress

# Create agents
agents = [
    InstitutionalAgent("Inst1", 2.0, 1.0),
    RetailAgent("Retail1", 0.5, 0.2),
    HFTAgent("HFT1", 0.1, 0.05)
]

market_state = {
    "expected_return": 0.01,
    "volatility": 0.03,
    "entropy": 1.2,
    "entropy_threshold": 1.0,
    "vol_threshold": 0.02,
    "order_imbalance": 0.3
}

positions = []
payoffs = []

for agent in agents:
    positions.append(agent.act(market_state))
    payoffs.append(payoff(agent, market_state))

stress = equilibrium_stress(payoffs)

print("POSITIONS:", positions)
print("EQUILIBRIUM STRESS:", stress)
