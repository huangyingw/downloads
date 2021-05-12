from itertools import product


class Solution:
    def letterCombinations(self, digits):
        mapping = {
            '2': "abc",
                        '3': "def",
                        '4': "ghi",
                        '5': "jkl",
                        '6': "mno",
                        '7': "pqrs",
                        '8': "tuv",
                        '9': "wxyz"}
        if not digits:
            return []
        return [''.join(combination) for combination in product(*(mapping[i] for i in digits), repeat=1)]

