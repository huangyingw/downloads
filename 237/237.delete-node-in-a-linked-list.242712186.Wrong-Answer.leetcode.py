class Solution(object):
    def deleteNode(self, node):
        if not node.next:
            node = None
        while node and node.next:
            node.val = node.next.val
            print('node before --> %s' % (node.val))
            node = node.next
            print('node before --> %s' % (node.val))

