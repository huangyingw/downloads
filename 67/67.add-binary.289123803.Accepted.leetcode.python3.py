class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        while i >= 0 or j >= 0 or carry > 0:
            ach = ord(a[i]) - ord('0') if i >= 0 else 0
            bch = ord(b[j]) - ord('0') if j >= 0 else 0
            res.append(str(ach ^ bch ^ carry))
            carry = (ach + bch + carry) >> 1  # It is equivalent to (a+b+c)/2
            i -= 1
            j -= 1
        return ''.join(res[::-1])

