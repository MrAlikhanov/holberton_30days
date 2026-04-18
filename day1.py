class Statistics:
    def __init__(self, data):
        self.data = sorted(data)
    
    def count(self):
        return len(self.data)
    
    def sum(self):
        return builtins_sum(self.data)
    
    def min(self):
        return self.data[0]
    
    def max(self):
        return self.data[-1]
    
    def range(self):
        return self.max() - self.min()
