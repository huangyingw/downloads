class Solution(object):
    def detectCycle(self, head):
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        print("slow --> %s" % slow.val)
        print("fast --> %s" % fast.val)
        while fast != head:
            fast = fast.next
            head = head.next
        return fast

