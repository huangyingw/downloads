import heapq


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        prev = dummy = ListNode(None)
        next_nodes, heap = [], []
        for i, node in enumerate(lists):
            next_nodes.append(node)
            if node:
                heap.append((node.val, i))
        heapq.heapify(heap)
        while heap:
            value, i = heapq.heappop(heap)
            node = next_nodes[i]
            prev.next = node
            prev = prev.next
            if node.next:
                next_nodes[i] = node.next
                heapq.heappush(heap, (node.next.val, i))
        return dummy.next

