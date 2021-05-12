import heapq


class Solution(object):
    def mergeKLists(self, lists):
        dummy = ListNode(-1)
        nav = dummy
        heap = [heapq.heappush(heap, (li.val, li)) for li in lists if li]
        while heap:
            smallest = heapq.heappop(heap)[1]
            nav.next = smallest
            nav = nav.next
            if smallest.next:
                heapq.heappush(heap, (smallest.next.val, smallest.next))
        return dummy.next

