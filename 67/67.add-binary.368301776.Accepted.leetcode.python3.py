class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ''
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
            if j >= 0:
                carry += int(b[j])
            carry, remainder = divmod(carry, 2)
            result = str(remainder) + result
            i -= 1
            j -= 1
        return result

