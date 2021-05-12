class Solution:
    def longestPalindrome(self, s):
        letter = [chr(i) for i in range(ord('a'), ord('z') + 1)] + [chr(j) for j in range(ord('A'), ord('Z') + 1)]
        result = 0
        for i in letter:
            result += s.count(i) // 2
        ind = 0
        for i in letter:
            if s.count(i) % 2 == 1:
                ind = 1
                break
        result = 2 * result + ind
        return result

