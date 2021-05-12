class Solution(object):
    def dfs(self, str, start, current, result):
        print("start --> %s" % start if start else 'start --> N')
        if start == len(str):
            result.append(list(current))


        for index in range(start, len(str)):
            subStr = str[start, index + 1]

            if self.isPalindrome(subStr):
                current.append(subStr)
                self.dfs(str, index + 1, current, result)
                current.pop(current.size() - 1)

    def isPalindrome(self, str):
        left = 0
        right = len(str) - 1

        while left < right:
            if str[left] != str[right]:
                return False

            left += 1
            right -= 1

        return True

    def partition(self, s):
        result = []
        self.dfs(s, 0, [], result)
        return result

