import pandas as pd
from core.state_space import MarketStateSpace
from core.entropy import MarketEntropy
from core.thermodynamics import MarketThermodynamics
from engine.regime import classify_regime
from engine.instability import instability_probability

# Load data
data = pd.read_csv("data/market_data.csv")
prices = data["Close"]

# Build state
state = MarketStateSpace(prices)
returns = state.returns.dropna()

# Entropy
entropy_engine = MarketEntropy(returns.values)
entropy_value = entropy_engine.shannon_entropy()

# Thermodynamics
vol = state.volatility.mean()
thermo = MarketThermodynamics(
    energy=vol,
    entropy=entropy_value,
    temperature=1.0
)

free_energy = thermo.free_energy()
entropy_rate = thermo.entropy_production_rate()

# Regime
regime = classify_regime([entropy_value], [vol])
instability = instability_probability(entropy_rate)

print("REGIME:", regime)
print("FREE ENERGY:", free_energy)
print("INSTABILITY RISK:", instability)
