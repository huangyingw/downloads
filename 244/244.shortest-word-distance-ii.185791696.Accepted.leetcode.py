class WordDistance(object):

    def __init__(self, words):
        self.w_to_idx = {}

        for idx, val in enumerate(words):
            self.w_to_idx.setdefault(val, []).append(idx)

    def shortest(self, word1, word2):
        distance = sys.maxint
        idxs1 = self.w_to_idx[word1]
        idxs2 = self.w_to_idx[word2]

        for idx1 in idxs1:
            for idx2 in idxs2:
                distance = min(distance, abs(idx1 - idx2))

        return distance

