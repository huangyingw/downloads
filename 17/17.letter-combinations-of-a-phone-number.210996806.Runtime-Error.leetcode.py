class Solution(object):
    def letterCombinations(self, digits):
        dic = [" ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        result = []

        if not digits:
            return result

        result.append("")

        if not digits:
            return result

        for i in range(0, len(digits)):
            letters = dic[digits[i] - '0']
            newRes = []

            for j in range(0, len(result)):
                for k in range(0, len(letters)):
                    newRes.append(result[j] + letters[k])
            result = newRes
        return result

