import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import numpy as np
from core.entropy import MarketEntropy
from core.thermodynamics import MarketThermodynamics
from engine.instability import instability_probability


import numpy as np
from core.entropy import MarketEntropy
from core.thermodynamics import MarketThermodynamics
from engine.instability import instability_probability

print("\n--- STAGE 1: NO-DATA CHECK ---")

# Synthetic abstract returns
returns_low = np.random.normal(0, 0.01, 1000)
returns_high = np.random.normal(0, 0.07, 1000)

e_low = MarketEntropy(returns_low).gaussian_entropy()
e_high = MarketEntropy(returns_high).gaussian_entropy()

print("Low entropy:", e_low)
print("High entropy:", e_high)

# Thermodynamic evolution
entropy = np.linspace(0.5, 2.5, 200)
energy = np.random.uniform(0.2, 0.3, 200)

thermo = MarketThermodynamics(
    energy=energy,
    entropy=entropy,
    temperature=1.0
)

free_energy = thermo.free_energy()
entropy_rate = thermo.entropy_production_rate()

instability = instability_probability(entropy_rate)

print("Final free energy:", free_energy[-1])
print("Instability probability:", instability)
from agents.institutional import InstitutionalAgent
from agents.retail import RetailAgent
from game.payoff import payoff
from game.equilibrium import equilibrium_stress

print("\n--- STAGE 2: AGENT CHECK (NO DATA) ---")

agents = [
    InstitutionalAgent("Inst", 2.0, 1.0),
    RetailAgent("Retail", 0.5, 0.2)
]

market_state = {
    "expected_return": 0.0,
    "volatility": 0.04,
    "entropy": 1.8,
    "entropy_threshold": 1.0,
    "vol_threshold": 0.02,
    "order_imbalance": 0.0
}

payoffs = [payoff(a, market_state) for a in agents]
stress = equilibrium_stress(payoffs)

print("Agent payoffs:", payoffs)
print("Equilibrium stress:", stress)
