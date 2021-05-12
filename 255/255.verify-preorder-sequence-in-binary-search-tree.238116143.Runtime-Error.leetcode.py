class Solution(object):
    def verifyPreorder(self, preorder):
        minV = -sys.maxint - 1
        stack = [-sys.maxint - 1]
        print('stack 1 --> %s' % stack)

        for num in preorder:
            if num < minV:
                return False

            while stack[-1] < num:
                minV = stack.pop()
                print('stack 2 --> %s' % stack)
            stack.append(num)

        return True

