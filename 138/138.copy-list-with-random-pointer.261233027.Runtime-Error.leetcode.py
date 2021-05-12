class Solution(object):
    def copyRandomList(self, head):
        node = head
        while node:
            next = node.next
            copy = Node(node.val, None, None)
            node.next = copy
            copy.next = next
            node = next
        node = head
        while node:
            if node.random:
                node.next.random = node.random.next
            node = node.next.next
        pseudo = prev = Node(0)
        node = head
        while node:
            prev.next = node.next
            node.next = node.next.next
            node = node.next
            prev = prev.next
        return pseudo.next

