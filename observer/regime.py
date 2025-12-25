class RegimeClassifier:
    def classify(self, entropy, entropy_rate):
        if entropy_rate < 0.01:
            return "ORDERED", 0.85
        elif entropy_rate < 0.03:
            return "TRANSITION", 0.75
        return "DISORDERED", 0.9
