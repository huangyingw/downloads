class Solution:
    def cloneGraph(self, node):
        if not node:
            return None
        old_to_new = {}
        newHead = UndirectedGraphNode(node.label)
        queue = [node]
        old_to_new[node] = newHead
        while queue:
            current = queue.pop()
            for neighbor in current.neighbors:
                if neighbor in old_to_new:
                    continue
                newNeighbor = UndirectedGraphNode(neighbor.label)
                old_to_new[neighbor] = newNeighbor
                old_to_new[current].neighbors.append(newNeighbor)
                queue.append(neighbor)
        return newHead

