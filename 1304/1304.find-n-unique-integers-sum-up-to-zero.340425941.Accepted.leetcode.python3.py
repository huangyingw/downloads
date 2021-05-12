class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        if n % 2 != 0:
            res.append(0)
            n -= 1
        n //= 2
        for i in range(1, n + 1):
            res.extend([-i, i])

        return res

