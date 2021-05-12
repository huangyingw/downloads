class Solution(object):
    def countAndSay(self, n):
        if n == 1:
            return "1"
        s = "1"
        for _ in range(n - 1):
            curVal, count, res = s[0], 0, []
            for i in s:
                if curVal == i:
                    count += 1
                else:
                    res.append(str(count))
                    res.append(curVal)
                    curVal = i
                    count = 1
            res.append(str(count))
            res.append(curVal)
            s = "".join(res)
        return s

