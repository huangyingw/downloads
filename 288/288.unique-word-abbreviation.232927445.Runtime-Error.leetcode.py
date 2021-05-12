class ValidWordAbbr(object):
    def __init__(self, dictionary):
        self.c2k = lambda s: s[0] + str(len(s) - 2) + s[-1]
        ab = [(self.c2k(s), s) for s in dictionary]
        d = dict()
        for k, v in ab:
            if not d.get(k):
                d[k] = set()
            d[k].add(v)
        self.d = d

    def isUnique(self, word):
        key = self.c2k(word)
        if not self.d.get(key):
            return True
        else:
            if word in self.d[key] and len(self.d[key]) == 1:
                return True

        return False

