import numpy as np
from observer.features import build_features
from observer.labels import label_regime
from observer.model import build_model

def train_observer(entropy, entropy_rate, free_energy, stress):
    X = build_features(entropy, entropy_rate, free_energy, stress)
    y = label_regime(entropy, entropy_rate)

    model = build_model()
    model.fit(X, y)

    return model
