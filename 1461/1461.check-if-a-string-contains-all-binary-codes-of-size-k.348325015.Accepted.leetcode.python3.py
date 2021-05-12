class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:

        return len({s[i - k: i] for i in range(k, len(s) + 1)}) == 2 ** k


class Solution1:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        binary_numbers = set()
        for i in range(2**k):
            binary_numbers.add(bin(i)[2:].zfill(k))

        temp = s[:k]
        if temp in binary_numbers:
            binary_numbers.remove(temp)
        for i in range(k, len(s)):
            temp = temp[1:] + s[i]
            if temp in binary_numbers:
                binary_numbers.remove(temp)

            if not binary_numbers:
                return True

        return False

