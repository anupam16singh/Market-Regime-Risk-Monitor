import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import numpy as np
from core.thermodynamics import MarketThermodynamics
from engine.instability import instability_probability
from observer.trainer import train_observer

print("\n--- STAGE 3: ML OBSERVER (NO DATA) ---")

# Synthetic system evolution
time = 300
entropy = np.linspace(0.5, 3.0, time)
entropy_rate = np.gradient(entropy)
energy = np.random.uniform(0.2, 0.3, time)
temperature = 1.0

thermo = MarketThermodynamics(
    energy=energy,
    entropy=entropy,
    temperature=temperature
)

free_energy = thermo.free_energy()

# Synthetic stress (agent conflict)
stress = entropy_rate**2 + np.random.normal(0, 0.01, time)

# Train observer
model = train_observer(
    entropy,
    entropy_rate,
    free_energy,
    stress
)

# Test prediction
test_state = [[
    entropy[-1],
    entropy_rate[-1],
    free_energy[-1],
    stress[-1]
]]

prediction = model.predict(test_state)

print("Predicted regime:", prediction[0])
