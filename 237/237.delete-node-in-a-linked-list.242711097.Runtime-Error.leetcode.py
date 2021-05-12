class Solution(object):
    def deleteNode(self, node):
        if not node.next:
            node = None
        while node.next:
            node.val = node.next.val
            print('node --> %' % (node))
            node = node.next
        node = None

