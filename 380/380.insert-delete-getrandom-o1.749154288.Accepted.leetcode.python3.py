class RandomizedSet(object):
    def __init__(self):
        self.values = []
        self.positions = {}

    def insert(self, val):
        if val not in self.positions:
            self.values.append(val)
            self.positions[val] = len(self.values) - 1
            return True
        return False

    def remove(self, val):
        if val in self.positions:
            valIdx, lastEle = self.positions[val], self.values[-1]
            self.positions[lastEle], self.values[valIdx] = valIdx, lastEle
            self.values.pop()
            self.positions.pop(val, 0)
            return True
        return False

    def getRandom(self):
        return self.values[random.randint(0, len(self.values) - 1)]

