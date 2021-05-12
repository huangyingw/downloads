import heapq


class Solution(object):
    def mergeKLists(self, lists):
        dummy = ListNode(-1)
        nav = dummy
        next_nodes = [(li.val, li) for li in lists if li]
        heapq.heapify(next_nodes)
        while next_nodes:
            smallest = heapq.heappop(next_nodes)[1]
            nav.next = smallest
            nav = nav.next
            if smallest.next:
                heapq.heappush(next_nodes, (smallest.next.val, smallest.next))
        return dummy.next

