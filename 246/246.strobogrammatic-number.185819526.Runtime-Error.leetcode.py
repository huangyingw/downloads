class Solution(object):
    def isStrobogrammatic(self, num):
        table = {'0': '0',
                 '1': '1',
                 '6': '9',
                 '8': '8',
                 '9': '6'
                 }
        newNum = ''

        for ch in num:
            newNum += table[ch]

        return num == newNum

