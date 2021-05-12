import heapq


class Solution(object):
    def mergeKLists(self, lists):
        dummy = ListNode(-1)
        nav = dummy
        heap = [(li.val, li) for li in lists if li]
        heapq.heapify(heap)
        while heap:
            smallest = heapq.heappop(heap)[1]
            nav.next = smallest
            nav = nav.next
            smallest = smallest.next
            if smallest:
                heapq.heappush(heap, (smallest.val, smallest))
        return dummy.next

