class Solution(object):
    def mergeTwoLists(self, l1, l2):
        nav = dummy = ListNode(-1)
        while l1 and l2:
            if l1.val < l2.val:
                nav.next = l1
                l1 = l1.next
            else:
                nav.next = l2
                l2 = l2.next
            nav = nav.next
        nav.next = l1 or l2
        return dummy.next

