import numpy as np

def run_agents(agents, market_state):
    positions = []
    payoffs = []

    for agent in agents:
        pos = agent.act(market_state)
        positions.append(pos)

    return np.array(positions)
