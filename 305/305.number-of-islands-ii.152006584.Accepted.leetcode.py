#
# [305] Number of Islands II
#
# https://leetcode.com/problems/number-of-islands-ii/description/
#
# algorithms
# Hard (39.74%)
# Total Accepted:    32.9K
# Total Submissions: 82.9K
# Testcase Example:  '3\n3\n[[0,0],[0,1],[1,2],[2,1]]'
#
# A 2d grid map of m rows and n columns is initially filled with water.
# We may perform an addLand operation which turns the water at position (row,
# col) into a land.
# Given a list of positions to operate, count the number of islands after each
# addLand operation.
# An island is surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.
#
# Example:
# Given m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]].
# Initially, the 2d grid grid is filled with water. (Assume 0 represents water
# and 1 represents land).
#
# 0 0 0
# 0 0 0
# 0 0 0
#
# Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.
#
# 1 0 0
# 0 0 0   Number of islands = 1
# 0 0 0
#
# Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.
#
# 1 1 0
# 0 0 0   Number of islands = 1
# 0 0 0
#
# Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.
#
# 1 1 0
# 0 0 1   Number of islands = 2
# 0 0 0
#
# Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.
#
# 1 1 0
# 0 0 1   Number of islands = 3
# 0 1 0
#
# We return the result as an array: [1, 1, 2, 3]
#
# Challenge:
# Can you do it in time complexity O(k log mn), where k is the length of the
# positions?
#


class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        def node_id(node, n):
            return node[0] * n + node[1]

        def find_set(x):
            if set[x] != x:
                set[x] = find_set(set[x])  # path compression.
            return set[x]

        def union_set(x, y):
            x_root, y_root = find_set(x), find_set(y)
            set[min(x_root, y_root)] = max(x_root, y_root)
        numbers = []
        number = 0
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        set = {}
        for position in positions:
            node = (position[0], position[1])
            set[node_id(node, n)] = node_id(node, n)
            number += 1
            for d in directions:
                neighbor = (position[0] + d[0], position[1] + d[1])
                if 0 <= neighbor[0] < m and 0 <= neighbor[1] < n and node_id(neighbor, n) in set:
                    if find_set(node_id(node, n)) != find_set(node_id(neighbor, n)):
                        # Merge different islands, amortised time: O(log*k) ~=
                        # O(1)
                        union_set(node_id(node, n), node_id(neighbor, n))
                        number -= 1
            numbers.append(number)
        return numbers

