class Solution(object):
    def insertionSortList(self, head):
        sorted_tail = dummy = ListNode(float('-inf'))
        dummy.next = head
        while sorted_tail.next:
            node = sorted_tail.next
            if node.val >= sorted_tail.val:
                sorted_tail = sorted_tail.next
                continue
            sorted_tail.next = sorted_tail.next.next
            insertion = dummy
            while insertion.next.val <= node.val:
                insertion = insertion.next
            node.next = insertion.next
            insertion.next = node
        return dummy.next

