class Solution(object):
    def canWin(self, s):
        for i in range(len(s) - 1):  # 寻找所有的翻转可能
            if s[i:i + 2] == "++":
                current = s[0:i] + "--" + s[i + 2:]  # 把找到的++变成--

                if not self.canWin(current):  # 看当前的字串是否存在边界，没有++了
                    return True  # 对手不能赢，那就是当前翻转的赢了
        return False  # loop中没有返回，不能赢，当前翻转的输了　　

