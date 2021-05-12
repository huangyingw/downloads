from collections import defaultdict


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        nb_prerequisites = defaultdict(int)
        prereq_list = defaultdict(list)
        for after, before in prerequisites:
            nb_prerequisites[after] += 1
            prereq_list[before].append(after)
        can_take = [idx for idx in range(numCourses) if nb_prerequisites[idx] == 0]
        while can_take:
            course = can_take.pop(0)
            numCourses -= 1
            for dependent in prereq_list[course]:
                nb_prerequisites[dependent] -= 1
                if nb_prerequisites[dependent] == 0:
                    can_take.append(dependent)
        return numCourses == 0

