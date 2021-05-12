class Solution(object):
    def shortestDistance(self, words, word1, word2):
        p1, p2, distance = -1, -1, sys.maxint
        for i in range(len(words)):
            if words[i] == word1:
                p1 = i
            if words[i] == word2:
                p2 = i
            distance = min(distance, abs(p1 - p2))
        return distance

