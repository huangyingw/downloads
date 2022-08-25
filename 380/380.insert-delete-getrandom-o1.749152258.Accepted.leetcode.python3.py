class RandomizedSet:
    def __init__(self):
        self.nums, self.pos = [], {}

    def insert(self, val):
        if val not in self.pos:
            self.nums.append(val)
            self.pos[val] = len(self.nums) - 1
            return True
        return False

    def remove(self, val):
        if val in self.pos:
            idx, v = self.pos[val], self.nums[-1]
            self.nums[idx], self.nums[-1] = self.nums[-1], self.nums[idx]
            self.pos[v] = idx
            self.nums.pop()
            del self.pos[val]
            return True
        return False

    def getRandom(self):
        return random.choice(self.nums)

