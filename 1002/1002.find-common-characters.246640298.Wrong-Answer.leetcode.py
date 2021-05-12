from collections import Counter


class Solution(object):
    def commonChars(self, A):
        counts = Counter(A[0])
        for word in A[1:]:
            word_count = Counter(word)
        result = []
        for char, count in counts.items():
            result += [char] * count
        return result

