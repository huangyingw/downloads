class Solution(object):
    def compress(self, chars):
        n = len(chars)
        idx = 0
        cnt = 1
        for i in range(1, n):
            if chars[i] == chars[i - 1]:
                cnt += 1
            else:
                chars[idx] = chars[i - 1]
                idx += 1
                if cnt > 1:
                    for j in str(cnt):
                        chars[idx] = j
                        idx += 1
                cnt = 1
        return idx

