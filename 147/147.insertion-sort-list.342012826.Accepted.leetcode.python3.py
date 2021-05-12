class Solution(object):
    def insertionSortList(self, head):
        if not head:
            return None
        sortedList = head
        head = head.next
        sortedList.next = None
        while head:
            cur = head
            head = head.next
            if cur.val <= sortedList.val:
                cur.next = sortedList
                sortedList = cur
            else:
                pre = sortedList
                while pre.next and pre.next.val < cur.val:
                    pre = pre.next
                cur.next = pre.next
                pre.next = cur
        return sortedList

