class InstabilityDetector:
    def __init__(self, entropy_rate, threshold=0.02):
        self.entropy_rate = entropy_rate
        self.threshold = threshold

    def probability(self):
        return min(1.0, self.entropy_rate / self.threshold)
