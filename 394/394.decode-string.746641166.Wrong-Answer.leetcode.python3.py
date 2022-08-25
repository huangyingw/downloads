class Solution:
    def decodeString(self, s):
        stack = []
        num = 0
        curString = ''
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(num)
                curString = ''
            elif c == ']':
                curNum = stack.pop()
                prevStr = stack.pop()
                curString = prevStr + curNum * curString
            elif c.isnumeric():
                num = num * 10 + int(c)
            else:
                curString += c
        return curString

