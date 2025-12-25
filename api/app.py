from fastapi import FastAPI
import numpy as np

from core.entropy import MarketEntropy
from core.energy import MarketEnergy
from core.instability import InstabilityDetector
from agents.stress import StructuralStress
from observer.regime import RegimeClassifier

app = FastAPI(title="THERMOQUANT MVP API")

@app.get("/regime_state")
def regime_state():
    returns = np.random.normal(0, 0.02, 500)

    entropy = MarketEntropy(returns).differential_entropy()
    entropy_rate = MarketEntropy(returns).entropy_rate()

    regime, confidence = RegimeClassifier().classify(entropy, entropy_rate)

    return {
        "regime": regime,
        "confidence": confidence
    }

@app.get("/stability")
def stability():
    returns = np.random.normal(0, 0.02, 500)

    entropy_engine = MarketEntropy(returns)
    entropy = entropy_engine.differential_entropy()
    entropy_rate = entropy_engine.entropy_rate()

    energy_engine = MarketEnergy(volatility=np.std(returns))
    free_energy = energy_engine.free_energy(entropy)

    instability = InstabilityDetector(entropy_rate).probability()

    level = "STABLE" if instability < 0.3 else "FRAGILE" if instability < 0.7 else "UNSTABLE"

    return {
        "stability_level": level,
        "instability_probability": round(instability, 3),
        "entropy": round(entropy, 3),
        "entropy_rate": round(entropy_rate, 4),
        "free_energy": round(free_energy, 3)
    }

@app.get("/structural_stress")
def structural_stress():
    agent_payoffs = [-1.2, -0.5, 0.1, 0.3]

    stress = StructuralStress(agent_payoffs)

    return {
        "stress_index": round(stress.stress_index(), 3),
        "stress_level": stress.stress_level()
    }

@app.get("/explain")
def explain():
    return {
        "primary_drivers": [
            "Entropy acceleration exceeded threshold",
            "Free energy turned negative",
            "Agent coordination degraded"
        ],
        "summary": "The market is structurally fragile due to rising uncertainty and coordination stress."
    }
