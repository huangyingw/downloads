class Solution(object):
    def findAnagrams(self, s, p):
        res = []
        if not s or not p:
            return res
        char_map = [0] * 256
        for c in p:
            char_map[ord(c)] += 1
        left, right, count = 0, 0, len(p)
        while right < len(s):
            if char_map[ord(s[right])] >= 1:
                count -= 1
            char_map[ord(s[right])] -= 1
            right += 1
            if count == 0:
                res.append(left)
            if right - left == len(p):
                if char_map[ord(s[left])] >= 0:
                    count += 1
                char_map[ord(s[left])] += 1
                left += 1
        return res

