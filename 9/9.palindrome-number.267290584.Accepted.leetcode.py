class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        ls = 0
        tmp = x
        while tmp != 0:
            ls += 1
            tmp = tmp // 10
        tmp = x
        for i in range(ls / 2):
            right = tmp % 10
            left = tmp / (10 ** (ls - 2 * i - 1))
            left = left % 10
            if left != right:
                return False
            tmp = tmp // 10
        return True

