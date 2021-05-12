

class Solution(object):
    def pathSum(self, root, vSum):
        def helper(node, vSum):
            count = 0
            if not node:
                return 0
            if vSum == 0:
                count += 1
            count += helper(node.left, vSum - node.val)
            count += helper(node.right, vSum - node.val)
            return count
        return helper(root, vSum) + helper(root.left, vSum) + helper(root.right, vSum)

