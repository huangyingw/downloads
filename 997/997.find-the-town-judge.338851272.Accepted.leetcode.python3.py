class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        graph = [0] * (N + 1)
        for t in trust:
            graph[t[0]] -= 1
            graph[t[1]] += 1
        for index in range(1, len(graph)):
            if graph[index] == N - 1:
                return index
        return -1

