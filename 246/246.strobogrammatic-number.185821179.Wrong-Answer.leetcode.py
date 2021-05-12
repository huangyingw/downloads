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
            if ch not in table:
                return False

            newNum += table[ch]

        return num == newNum

