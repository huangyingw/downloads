class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        adjacencyList = {}
        inCount = [0] * numCourses

        for prerequisite in prerequisites:
            adjacencyList.setdefault(
                prerequisite[1], []).append(prerequisite[0])
            inCount[prerequisite[0]] += 1

        queue = [idx for idx in range(numCourses) if inCount[idx] == 0]
        result = []

        while queue:
            top = queue.pop(0)
            result.append(top)

            for a in adjacencyList.get(top, []):
                inCount[a] -= 1

                if inCount[a] == 0:
                    queue.append(a)

        return result if len(result) == numCourses else []

