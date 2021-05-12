class Solution:
    def isPalindrome(self, x):
        str_x = str(x)
        left = 0
        right = len(str_x) - 1
        while left < right:
            if str_x[left] == str_x[right]:
                left += 1
                right -= 1
            else:
                return False
        return True

