class Solution(object):
    def strobogrammaticInRange(self, low, high):
        if int(low) >= int(high):
            return 1 if low == high else 0  # 特殊边界情况处理
        if len(low) == len(high):  # 上边界与下边界数字长度相等
            arr = self.findStrobogrammatic(len(low))
            return len(list(filter(lambda c: low <= c <= high, arr)))
        else:  # 如果不相等，求出中间所有n位数的情况，len(low) <= n <= len(high)
            res = 0
            for i in range(len(low), len(high) + 1):
                arr = self.findStrobogrammatic(i)
                if i == len(low):
                    res += len(list(filter(lambda c: low <= c, arr)))
                elif i == len(high):
                    res += len(list(filter(lambda c: c <= high, arr)))
                else:
                    res += len(arr)
            return res

    def findStrobogrammatic(self, n):
        def dfs(arr, length, curLen, curString, isOdd):
            elements = ['0', '1', '6', '8', '9']
            # 要生成对应的数字，例如: "198"(odd) => "19861", "68"(even)=>"6886"
            if curLen == length:
                d = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
                if isOdd:
                    for i in curString[:-1][::-1]:
                        curString += d[i]
                else:
                    for i in curString[::-1]:
                        curString += d[i]
                arr.append(curString)
                return

            if curLen < length:
                if curLen == length - 1 and isOdd:
                    for i in ['0', '1', '8']:
                        dfs(arr, length, curLen + 1, curString + i, isOdd)

                elif curLen == 0:
                    for i in elements[1:]:
                        dfs(arr, length, curLen + 1, curString + i, isOdd)

                else:
                    for i in elements:
                        dfs(arr, length, curLen + 1, curString + i, isOdd)

        arr = []
        if n % 2 == 0:
            dfs(arr, n // 2, 0, "", False)
        else:
            dfs(arr, (n + 1) // 2, 0, "", True)

        return arr

