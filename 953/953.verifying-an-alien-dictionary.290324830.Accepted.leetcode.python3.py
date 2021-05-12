class Solution(object):
    def isAlienSorted(self, words, order):
        order_map = {}
        for i, v in enumerate(order):
            order_map[v] = i

        def cmp_alien(x, y):
            ls = min(len(x), len(y))
            index = 0
            while index < ls:
                if x[index] != y[index]:
                    return order_map[x[index]] - order_map[y[index]]
                index += 1
            return len(x) - len(y)
        pos = 0
        while pos + 1 < len(words):
            if cmp_alien(words[pos], words[pos + 1]) > 0:
                return False
            pos += 1
        return True

