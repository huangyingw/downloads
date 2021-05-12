class Solution(object):
    def verifyPreorder(self, preorder):
        minV = -sys.maxint - 1
        stack = [sys.maxint]

        for num in preorder:
            if num < minV:
                return False

            stack.append(num)

        return True

