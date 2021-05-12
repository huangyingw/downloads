class Solution(object):
    def removeElements(self, head, val):
        dummy = ListNode(-1)
        dummy.next = head
        current = dummy
        print('current --> %s' % current.val if current else 'null')

        while current.next:
            if current.next.val == val:
                current.next = current.next.next
                print('current.next --> %s' %
                      current.next.val if current.next else 'null')
            else:

                current = current.next
                print('current --> %s' % current.val if current else 'null')
        return dummy.next

