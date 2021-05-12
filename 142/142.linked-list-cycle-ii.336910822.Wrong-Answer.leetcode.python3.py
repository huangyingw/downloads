class Solution(object):
    def detectCycle(self, head):
        fast = slow = head
        while fast and fast.next and fast != slow:
            fast = fast.next.next
            slow = slow.next
        print('slow --> %s' % slow)
        print('fast --> %s' % fast)
        while fast != head:
            fast = fast.next
            head = head.next
        return fast

