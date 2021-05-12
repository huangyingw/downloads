class Solution(object):
    def insertionSortList(self, head):
        sortedList = head
        head = head.next
        sortedList.next = None
        while head:
            curr = head
            head = head.next
            if curr.val <= sortedList.val:
                curr.next = sortedList
                sortedList = curr
            else:
                temp = sortedList
                while temp.next and temp.next.val < curr.val:
                    temp = temp.next
                curr.next = temp.next
                temp.next = curr
        return sortedList

