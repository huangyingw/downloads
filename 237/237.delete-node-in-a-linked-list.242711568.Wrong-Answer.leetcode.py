class Solution(object):
    def deleteNode(self, node):
        if not node.next:
            node = None
        while node.next:
            node.val = node.next.val
            print('node before --> %s' % (node.val))
            node = node.next
            print('node next --> %s' % (node.val))
        node = None

