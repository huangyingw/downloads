class Solution:
    def cloneGraph(self, node):
        old_to_new = {}
        newHead = Node(node.val, [])
        queue = [node]
        old_to_new[node] = newHead
        while queue:
            current = queue.pop()
            for neighbor in current.neighbors:
                if neighbor in old_to_new:
                    continue
                newNeighbor = Node(neighbor.val, [])
                old_to_new[current].neighbor.append(newNeighbor)
                queue.append(neighbor)
        return newHead

