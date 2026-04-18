def mean(self):
        return round(sum(self.data) / self.count())
    
    def median(self):
        n = self.count()
        mid = n // 2
        if n % 2 == 0:
            return (self.data[mid - 1] + self.data[mid]) / 2
        return self.data[mid]
    
    def mode(self):
        freq = {}
        for val in self.data:
            freq[val] = freq.get(val, 0) + 1
        max_count = max(freq.values())
        mode_val = [k for k, v in freq.items() if v == max_count][0]
        return (mode_val, max_count)
