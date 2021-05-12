class Solution(object):
    def deleteNode(self, node):
        if not node.next:
            node = None
        current = None
        while node.next:
            node.val = node.next.val
            print('node before --> %s' % (node.val))
            current = node
            node = node.next
            print('node next --> %s' % (node.val))
        current.next = None

