class Solution(object):
    def longestCommonPrefix(self, strs):
        def prefix(strs, index):
            check_prefix = strs[0][:index]
            for index in range(1, len(strs)):
                if not strs[index].startswith(check_prefix):
                    return False
            return True
        minLength = float('inf')
        for string in strs:
            minLength = min(minLength, len(string))
        low, high = 0, minLength
        while low <= high:
            mid = (low + high) // 2
            if (prefix(strs, mid)):
                low = mid + 1
            else:
                high = mid - 1
        return strs[0][:(low + high) // 2]

