class Solution(object):
    def insertionSortList(self, head):
        dummy = ListNode(0)
        pre = dummy
        cur = head
        nextNode = None

        while cur:
            pre = dummy

            while pre.next and pre.next.val < cur.val:
                pre = pre.next
            nextNode = cur.next
            cur.next = pre.next
            pre.next = cur
            cur = nextNode
        return dummy.next

