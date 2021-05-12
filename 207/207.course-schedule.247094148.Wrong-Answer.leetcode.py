class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        adjacencyList = {}
        inCount = [0] * numCourses
        for prerequisite in prerequisites:
            adjacencyList.setdefault(prerequisite[1], []).append(prerequisite[0])
        queue = [idx for idx in range(numCourses) if inCount[idx] == 0]
        while queue:
            top = queue.pop(0)
            for a in adjacencyList.get(top, []):
                inCount[a] -= 1
                if inCount[a] == 0:
                    queue.append(a)
        return not [idx for idx in range(numCourses) if inCount[idx] != 0]

