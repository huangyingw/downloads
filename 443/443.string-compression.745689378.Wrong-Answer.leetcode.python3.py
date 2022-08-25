class Solution(object):
    def compress(self, chars):
        n = len(chars)
        idx = 0
        cnt = 1
        for i in range(1, n + 1):
            if i < n and chars[i] == chars[i - 1]:
                print("i --> %s" % chars[i])
                cnt += 1
            else:
                idx += 1
                if cnt > 1:
                    print("idx --> %s" % idx)
                    print("chars[idx] --> %s" % chars[idx])
                    for j in str(cnt):
                        chars[idx] = j
                        idx += 1
                cnt = 1
        return idx

