"""
Given a collection of intervals, merge all overlapping intervals.
Example 1:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:
Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""
import collections


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def overlap(self, a, b):
        return a.start <= b.end and b.start <= a.end

    def build_graph(self, intervals):
        graph = collections.defaultdict(list)
        for i, interval_i in enumerate(intervals):
            for j in range(i + 1, len(intervals)):
                if self.overlap(interval_i, intervals[j]):
                    graph[interval_i].append(intervals[j])
                    graph[intervals[j]].append(interval_i)
        return graph

    def merge_nodes(self, nodes):
        min_start = min(node.start for node in nodes)
        max_end = max(node.end for node in nodes)
        return Interval(min_start, max_end)

    def get_components(self, graph, intervals):
        visited = set()
        comp_number = 0
        nodes_in_comp = collections.defaultdict(list)

        def mark_component_dfs(start):
            stack = [start]
            while stack:
                node = stack.pop()
                if node not in visited:
                    visited.add(node)
                    nodes_in_comp[comp_number].append(node)
                    stack.extend(graph[node])

        for interval in intervals:
            if interval not in visited:
                mark_component_dfs(interval)
                comp_number += 1
        return nodes_in_comp, comp_number

    def merge(self, intervals):
        graph = self.build_graph(intervals)
        nodes_in_comp, number_of_comps = self.get_components(graph, intervals)

        return [self.merge_nodes(nodes_in_comp[comp]) for comp in range(number_of_comps)]


class Solution2:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x.start)
        merged = []
        for interval in intervals:

            if not merged or merged[-1].end < interval.start:
                merged.append(interval)
            else:

                merged[-1].end = max(merged[-1].end, interval.end)
        return merged

