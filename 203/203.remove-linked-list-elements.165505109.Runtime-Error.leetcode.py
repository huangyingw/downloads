class Solution(object):
    def removeElements(self, head, val):
        dummy = ListNode(-1)
        dummy.next = head
        current = dummy
        print('current --> %s' % current.val)

        while current.next:
            if current.next.val == val:
                current.next = current.next.next

            current = current.next
            print('current --> %s' % current.val)
        return dummy.next

