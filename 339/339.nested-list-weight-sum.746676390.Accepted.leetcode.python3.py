class Solution(object):
    def depthSum(self, nestedList):
        def helper(nested, depth):
            total = 0
            for item in nested:
                if item.isInteger():
                    total += depth * item.getInteger()
                else:
                    total += helper(item.getList(), depth + 1)
            return total
        return helper(nestedList, 1)

