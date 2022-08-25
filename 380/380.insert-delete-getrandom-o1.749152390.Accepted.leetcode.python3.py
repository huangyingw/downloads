class RandomizedSet(object):
    def __init__(self):
        self.mapping = {}
        self.items = []

    def insert(self, val):
        if val not in self.mapping:
            self.items.append(val)
            self.mapping[val] = len(self.items) - 1
            return True
        return False

    def remove(self, val):
        if val not in self.mapping:
            return False
        index = self.mapping[val]
        self.items[index] = self.items[-1]
        self.mapping[self.items[index]] = index
        self.items.pop()
        del self.mapping[val]
        return True

    def getRandom(self):
        return self.items[random.randint(0, len(self.items) - 1)]

