class Solution(object):
    def verifyPreorder(self, preorder):
        min = -sys.maxint - 1
        stack = []

        for num in preorder:
            if num < min:
                return False

            while stack[-1] < num:
                min = stack.pop()
            stack.append(num)

        return True

