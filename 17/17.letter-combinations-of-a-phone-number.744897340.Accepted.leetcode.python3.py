class Solution(object):
    def letterCombinations(self, digits):
        dic = [" ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        result = []
        if not digits:
            return result
        result.append("")
        for i in range(len(digits)):
            letters = dic[ord(digits[i]) - ord('0')]
            newRes = []
            for j in range(len(result)):
                for k in range(len(letters)):
                    newRes.append(result[j] + letters[k])
            result = newRes
        return result

