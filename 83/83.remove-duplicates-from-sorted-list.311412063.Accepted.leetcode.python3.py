class Solution(object):
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head
        root, tail, head = head, head, head.next
        while head:
            if head.val != tail.val:
                tail.next = head
                tail = tail.next
            head = head.next
        tail.next = None
        return root

