from collections import defaultdict


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        nb_prerequisites = defaultdict(int)
        prereq_list = defaultdict(list)
        can_take = set(i for i in range(numCourses)) - set(nb_prerequisites.keys())
        while can_take:
            course = can_take.pop()
            numCourses -= 1
            for dependent in prereq_list[course]:
                nb_prerequisites[dependent] -= 1
                if nb_prerequisites[dependent] == 0:
                    can_take.add(dependent)
        return numCourses == 0

