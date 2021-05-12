class Solution(object):

    def canBreak(self, s, wordDict):
        can_make = [False] * (len(s) + 1)
        can_make[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i - 1, -1, -1):
                if can_make[j] and s[j:i] in wordDict:
                    can_make[i] = True
                    break
        return can_make[-1]

    def wordBreak(self, s, wordDict):
        if not self.canBreak(s, wordDict):
            return []
        result_lists = self.break_word(s, 0, wordDict, {})
        return [" ".join(result) for result in result_lists]

    def break_word(self, s, left, wordDict, memo):

        if left >= len(s):
            return [[]]
        if left in memo:
            return memo[left]

        results = []
        for i in range(left + 1, len(s) + 1):
            prefix = s[left:i]
            suffix_breaks = self.break_word(s, i, wordDict, memo)
            if suffix_breaks and prefix in wordDict:
                for suffix_break in suffix_breaks:
                    results.append([prefix] + suffix_break)

        return results

