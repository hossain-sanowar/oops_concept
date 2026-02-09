class StandardScalerStep:
    def fit(self,data):
        self.mean = sum(data) / len(data)
        self.var = sum((x - self.mean) ** 2 for x in data) / len(data)
        self.std = self.var ** 0.5 if self.var > 0 else 1.0
        return self

    def transform(self, data): return [(x - self.mean) / self.std for x in data]

class ThresholdStep:
    def __init__(self, threshold):
        self.threshold = threshold

    def fit(self, data):
        return self  # nothing to learn

    def transform(self, data):
        return [x for x in data if x > self.threshold]

class Pipeline:
    def __init__(self, steps):
        self.steps = steps