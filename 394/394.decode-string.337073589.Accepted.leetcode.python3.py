class Solution:
    def decodeString(self, s):
        numStack = strStack = []
        num = 0
        curString = ''
        for c in s:
            if c == '[':
                strStack.append(curString)
                numStack.append(num)
                curString = ''
                num = 0
            elif c == ']':
                curNum = numStack.pop()
                prevStr = strStack.pop()
                curString = prevStr + curNum * curString
            elif c.isnumeric():
                num = num * 10 + int(c)
            else:
                curString += c
        return curString

