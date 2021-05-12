class Solution:
    def numSteps(self, s: str) -> int:
        count = carry = 0
        for i in range(len(s) - 1, 0, -1):
            count += 1
            if (s[i] == '0' and carry == 1) or (s[i] == '1' and carry == 0):
                carry = 1
                count += 1
        return count + carry

