class Solution(object):
    def generatePalindromes(self, s):
        dic = {}
        half = []
        res = []
        for c in s:
            dic[c] = dic.get(c, 0) + 1
        odd = 0
        for c in dic:
            if dic[c] % 2 != 0:
                odd += 1
        if odd > 1:
            return []
        seed = []
        mid = ''
        for c in dic:
            if dic[c] % 2 == 1:
                mid = c
            seed.extend([c] * (dic[c] // 2))
        self.dfs(seed, half, [])
        for r in half:
            res.append(''.join(r) + mid + ''.join(reversed(r)))
        return res

    def dfs(self, seed, half, permutation):
        if not seed:
            half.append(permutation)
        for i in range(len(seed)):
            self.dfs(seed[:i] + seed[i + 1:], half, permutation + [seed[i]])

