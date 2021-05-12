class Solution(object):
    def compress(self, chars):
        n = len(chars)
        idx = 0
        cnt = 0
        for i in range(n):
            cnt += 1
            if (i + 1 >= n) or (chars[i] != chars[i + 1]):
                chars[idx] = chars[i]
                idx += 1
                if cnt > 1:
                    for j in str(cnt):
                        chars[idx] = j
                        idx += 1
                cnt = 0
        return idx

