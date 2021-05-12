class WordDistance(object):

    def __init__(self, words):
        self.w_to_idx = {}

        for idx, val in enumerate(words):
            self.w_to_idx.setdefault(val, []).append(idx)

    def shortest(self, word1, word2):
        distance = sys.maxint
        idxs1 = self.w_to_idx[word1]
        idxs2 = self.w_to_idx[word2]
        idx1, idx2 = 0, 0

        while idx1 < len(idxs1) and idx2 < len(idxs2):
            distance = min(distance, abs(idxs1[idx1] - idxs2[idx2]))

            if idxs1[idx1] < idxs2[idx2]:
                idx1 += 1
            else:
                idx2 += 1

        return distance

