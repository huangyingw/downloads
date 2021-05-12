class Solution:

    def findAndReplacePattern(self, words, pattern):

        patter_list = [pattern.find(i) for i in pattern]

        def is_iso(word):
            return [word.find(j) for j in word] == patter_list
        return list(filter(is_iso, words))

