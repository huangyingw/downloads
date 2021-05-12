class Solution(object):
    def isAlienSorted(self, words, order):
        d = {v: i for i, v in enumerate(order)}
        encode_words = []
        encode_words = [[d[l] for l in word] for word in words]
        return sorted(encode_words) == encode_words

