class Solution:
    def deleteDuplicates(self, head):
        dummy = prev = ListNode(0)
        dummy.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head
            prev = prev.next
            head = head.next
        return dummy.next

