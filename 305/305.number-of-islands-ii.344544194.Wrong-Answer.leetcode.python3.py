class Solution(object):
    def numIslands2(self, m, n, positions):
        def node_id(node, n):
            return node[0] * n + node[1]

        def find_set(x):
            if roots[x] != x:
                roots[x] = find_set(roots[x])
            return roots[x]

        def union_set(x, y):
            x_root, y_root = find_set(x), find_set(y)
            roots[min(x_root, y_root)] = max(x_root, y_root)
        numbers = []
        number = 0
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        roots = {}
        for position in positions:
            node = (position[0], position[1])
            roots[node_id(node, n)] = node_id(node, n)
            number += 1
            for d in directions:
                neighbor = (position[0] + d[0], position[1] + d[1])
                if 0 <= neighbor[0] < m and 0 <= neighbor[1] < n and node_id(neighbor, n) in roots:
                    if find_set(node_id(node, n)) != find_set(node_id(neighbor, n)):
                        union_set(node_id(node, n), node_id(neighbor, n))
                        number -= 1
            numbers.append(number)
        return numbers

