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

    def fit(self, data):
        for step in self.steps:
            step.fit(data)
            data = step.transform(data)
        return self

    def transform(self, data):
        for step in self.steps:
            data = step.transform(data)
        return data

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pipe = Pipeline([StandardScalerStep(), ThresholdStep(threshold=0.5)])
pipe.fit(data)
print(pipe.transform(data))


class list:
    def __init__(self, data):
        self.data = data
