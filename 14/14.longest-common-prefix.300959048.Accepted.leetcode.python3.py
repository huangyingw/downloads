class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res = strs[0]
        length = len(res)
        for i in range(1, len(strs)):
            index = 0
            while index < length and index < len(strs[i]):
                if res[index] != strs[i][index]:
                    break
                index += 1
            if not index:
                return ""
            length = index
        return res[:length]

