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


"""
n = 1, [0]
n = 2, [-1, 1]
n = 3, [-2, 0, 2]
n = 4, [-3, -1, 1, 3]
n = 5, [-4, -2, 0, 2, 4]
Explanation
Find the rule
A[i] = i * 2 - n + 1
"""


class Solution1:
    def sumZero(self, n: int) -> List[int]:
        return [i for i in range(1 - n, n, 2)]

