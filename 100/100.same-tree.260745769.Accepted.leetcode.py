class Solution(object):
    def isSameTree(self, p, q):
        stack = [(p, q)]
        while stack:
            node1, node2 = stack.pop()
            if node1 and node2 and node1.val == node2.val:
                stack += [(node1.left, node2.left)]
                stack += [(node1.right, node2.right)]
            else:
                if node1 != node2:
                    return False
        return True

