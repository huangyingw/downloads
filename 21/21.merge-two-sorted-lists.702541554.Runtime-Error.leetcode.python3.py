class Solution(object):
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(-1)
        nav = dummy
        heap = []
        for li in [l1, l2]:
            if li:
                heapq.heappush(heap, (li.val, li))
        while heap:
            smallest = heapq.heappop(heap)[1]
            nav.next = smallest
            nav = nav.next
            smallest = smallest.next
            if smallest:
                heapq.heappush(heap, (smallest.val, smallest))
        return dummy.next

