class Solution(object):
    def dfs(self, s, start, current, result):
        print("s --> %s" % s if s else 's --> N')
        print("start --> %s" % start)
        print("current --> %s" % current if current else 'current --> N')
        if start == len(s):
            result.append(list(current))

        for index in range(start, len(s)):
            subStr = s[start, index + 1]

            if self.isPalindrome(subStr):
                current.append(subStr)
                self.dfs(s, index + 1, current, result)
                current.pop(current.size() - 1)

    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True

    def partition(self, s):
        result = []
        self.dfs(s, 0, [], result)
        return result

