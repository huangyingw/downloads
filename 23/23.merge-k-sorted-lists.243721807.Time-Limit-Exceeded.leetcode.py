import heapq


class Solution(object):
    def mergeKLists(self, lists):
        dummy = ListNode(-1)
        nav = dummy
        heap = []
        for li in lists:
            heapq.heappush(heap, (li.val, li))
        while heap:
            smallest = heapq.heappop(heap)[1]
            nav.next = smallest
            nav = nav.next
            if smallest.next:
                heapq.heappush(heap, (smallest.val, smallest))
        return dummy.next

