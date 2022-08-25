class Solution(object):
    def deleteNode(self, node):
        while node.next:
            node.val = node.next.val
            current = node
            node = node.next
        print("node --> %s" % node.val)
        current.next = None

