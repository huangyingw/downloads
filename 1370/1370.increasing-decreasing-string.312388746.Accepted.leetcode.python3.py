class Solution:
    def sortString(self, s: str) -> str:
        alphabets = [0] * 26
        for c in s:
            alphabets[ord(c) - ord('a')] += 1

        res = []
        flag = direction = True
        index = 0
        while flag:
            flag = False
            while (index < len(alphabets) and direction) or (index >= 0 and not direction):
                if alphabets[index] > 0:
                    res.append(chr(index + ord('a')))
                    alphabets[index] -= 1
                    flag = True
                index += 1 if direction else -1
            direction = False if direction else True
            index += 1 if direction else -1
        return "".join(res)

