class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        idx1, idx2, distance, turn, inc = -1, -1, sys.maxint, 0, 1 if word1 == word2 else 0

        for i in range(len(words)):
            if words[i] == word1 and turn % 2 == 0:
                idx1 = i

                if idx2 != -1:
                    distance = min(distance, idx1 - idx2)

                turn += inc
            elif words[i] == word2:
                idx2 = i

                if idx1 != -1:
                    distance = min(distance, idx2 - idx1)

                turn += inc
        return distance

