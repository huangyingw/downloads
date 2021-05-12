class Solution:
    def cloneGraph(self, node):
        if not node:
            return None
        queue = []
        neighbor_to_copy = {}
        newHead = Node(node.val, [])
        queue.append(node)
        neighbor_to_copy.put(node, newHead)
        while queue:
            curr = queue.pop()
            currNeighbors = curr.neighbors
            for aNeighbor in currNeighbors:
                if aNeighbor not in neighbor_to_copy:
                    copy = Node(aNeighbor.val, [])
                    neighbor_to_copy.put(aNeighbor, copy)
                    queue += [aNeighbor]
                neighbor_to_copy.get(curr).neighbors += [neighbor_to_copy.get(aNeighbor)]
        return newHead

