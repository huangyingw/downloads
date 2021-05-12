class Solution(object):
    def deleteNode(self, node):
        if not node.next:
            node = None

        while node.next:
            node.val = node.next.val
            node = node.next

        node.next = None

