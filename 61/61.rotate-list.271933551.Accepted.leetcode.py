class Solution(object):
    def rotateRight(self, head, k):
        if not head:
            return
        count = 1
        node = head
        while node.next:
            node = node.next
            count += 1
        node.next = head
        to_move = count - (k % count)
        while to_move > 0:
            node = node.next
            to_move -= 1
        head = node.next
        node.next = None
        return head

