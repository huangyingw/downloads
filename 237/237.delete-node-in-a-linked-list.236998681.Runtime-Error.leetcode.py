class Solution(object):
    def deleteNode(self, node):
        if not node.next:
            node = None

        while node:
            node.val = node.next.val
            node = node.next

