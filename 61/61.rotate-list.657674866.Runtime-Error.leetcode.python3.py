class Solution:
    def rotateRight(self, head, k):
        if not head:
            return []
        l = 1
        dummy = head
        while dummy.next:
            l += 1
            dummy = dummy.next
        k = k % l
        tail = dummy
        tail.next = head
        print("tail --> %s" % tail.val)
        for i in range(l - k):
            tail = tail.next
        new_head = tail.next
        tail.next = None
        print("new_head --> %s" % new_head.val)
        return new_head

