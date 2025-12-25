import numpy as np

def label_regime(entropy, entropy_rate):
    labels = []

    for e, de in zip(entropy, entropy_rate):
        if e < np.percentile(entropy, 30) and de < 0.01:
            labels.append(0)   # ORDERED
        elif e < np.percentile(entropy, 70):
            labels.append(1)   # TRANSITION
        else:
            labels.append(2)   # DISORDERED

    return np.array(labels)
