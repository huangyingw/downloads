class Solution(object):
    def titleToNumber(self, s):
        result = 0

        for char in s:
            result = result * 26 + ord(char) - ord('A') + 1
        return result

