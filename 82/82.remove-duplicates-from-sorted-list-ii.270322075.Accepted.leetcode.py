class Solution(object):
    def deleteDuplicates(self, head):
        pseudo = prev = ListNode(None)
        pseudo.next = head
        node = head
        while node:
            if node.next and node.val == node.next.val:
                duplicate_value = node.val
                node = node.next
                while node and node.val == duplicate_value:
                    node = node.next
                prev.next = None
            else:
                prev.next = node
                prev = node
                node = node.next
        return pseudo.next

