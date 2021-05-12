class Solution(object):
    def mergeTwoLists(self, l1, l2):
        pos = dummyHead = ListNode(-1)
        while l1 and l2:
            if l1.val <= l2.val:
                pos.next = l1
                l1 = l1.next
            else:
                pos.next = l2
                l2 = l2.next
            pos = pos.next
        if l1 is not None:
            pos.next = l1
        if l2 is not None:
            pos.next = l2
        return dummyHead.next

