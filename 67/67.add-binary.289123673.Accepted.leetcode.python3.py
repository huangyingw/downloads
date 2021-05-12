class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        while i >= 0 or j >= 0:
            ach = int(a[i]) if i >= 0 else 0
            bch = int(b[j]) if j >= 0 else 0
            summ = ach + bch + carry
            res.append(str(summ % 2))
            carry = 1 if summ > 1 else 0
            i -= 1
            j -= 1
        if carry == 1:
            res.append(str(carry))
        return ''.join(res[::-1])

