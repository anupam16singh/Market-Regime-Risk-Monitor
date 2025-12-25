import numpy as np

def payoff(agent, market_state):
    return agent.utility(
        expected_return=market_state["expected_return"],
        volatility=market_state["volatility"],
        entropy=market_state["entropy"]
    )
