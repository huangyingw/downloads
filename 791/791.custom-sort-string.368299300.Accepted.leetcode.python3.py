from collections import Counter


class Solution:

    def customSortString(self, S, T):

        c = Counter(T)
        lefted = c.keys() - set(S)
        return ''.join(letter * c[letter] for letter in ([s for s in S] + [l for l in lefted]))

