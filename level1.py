import math

class Statistics:
    def __init__(self, data):
        self.data = sorted(data)
        self.n = len(data)

    def count(self):
        return self.n

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return self.max() - self.min()

    def mean(self):
        return round(self.sum() / self.n)

    def median(self):
        mid = self.n // 2
        if self.n % 2 == 0:
            return (self.data[mid - 1] + self.data[mid]) / 2
        return self.data[mid]

    def mode(self):
        counts = {}
        for x in self.data:
            counts[x] = counts.get(x, 0) + 1
        mode_val = max(counts, key=counts.get)
        return {'mode': mode_val, 'count': counts[mode_val]}

    def var(self):
        mu = self.mean()
        return round(sum((x - mu) ** 2 for x in self.data) / self.n, 1)

    def std(self):
        return round(math.sqrt(self.var()), 1)

    def freq_dist(self):
        counts = {}
        for x in self.data:
            counts[x] = counts.get(x, 0) + 1
        # Convert to percentage and sort
        dist = [(round((count / self.n) * 100, 1), val) for val, count in counts.items()]
        return sorted(dist, reverse=True)

    def describe(self):
        return (f"Count: {self.count()}\nSum: {self.sum()}\nMin: {self.min()}\n"
                f"Max: {self.max()}\nRange: {self.range()}\nMean: {self.mean()}\n"
                f"Median: {self.median()}\nMode: {self.mode()}\nVariance: {self.var()}\n"
                f"Standard Deviation: {self.std()}\nFrequency Distribution: {self.freq_dist()}")

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)
print(data.describe())
