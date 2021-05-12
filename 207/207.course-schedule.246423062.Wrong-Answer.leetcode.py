class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        visited = [False for _ in range(numCourses)]
        stack = [False for _ in range(numCourses)]
        for pair in prerequisites:
            x, y = pair
            graph[x].append(y)
        for course in range(numCourses):
            if visited[course] == False:
                if self.dfs(graph, visited, stack, course):
                    return False
        return True

    def dfs(self, graph, visited, stack, course):
        visited[course] = True
        stack[course] = True
        for neigh in graph[course]:
            if visited[neigh] == False:
                if self.dfs(graph, visited, stack, neigh):
                    return True
            elif stack[neigh]:
                return True
        return False

