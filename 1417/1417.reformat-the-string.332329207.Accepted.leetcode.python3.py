class Solution:
    def reformat(self, s: str) -> str:
        i = j = 0
        res = []
        count_digit = count_alphabet = 0
        for c in s:
            if 'a' <= c <= 'z':
                count_alphabet += 1
            else:
                count_digit += 1
        if abs(count_digit - count_alphabet) > 1:
            return ""
        while i < len(s) and j < len(s):
            while i < len(s) and s[i].isdigit():
                i += 1
            while j < len(s) and 'a' <= s[j] <= 'z':
                j += 1
            if i < len(s) and len(res) % 2 == 0:
                res.append(s[i])
                i += 1
            if j < len(s) and len(res) % 2 != 0:
                res.append(s[j])
                j += 1
        if len(res) != len(s):
            if j < len(s):
                res.insert(0, s[j])
            else:
                res.append(s[i])
        return "".join(res)

