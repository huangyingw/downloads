class Solution(object):
    def insertionSortList(self, head):
        dummy = ListNode(-1)
        dummy.next = head
        current = dummy

        while current:
            pre = dummy

