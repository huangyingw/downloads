class Solution(object):
    def verifyPreorder(self, preorder):
        min = -sys.maxint - 1
        stack = []

        for num in preorder:
            print("num --> %s\n" % num)
            if num < min:
                return False

            while stack and stack[-1] < num:
                min = stack.pop()
                print("min --> %s\n" % min)

            stack.append(num)
            print("stack --> %s\n" % stack)

        return False

