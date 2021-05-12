class Solution(object):
    def getImportance(self, employees, query_id):
        emap = {e.id: e for e in employees}

        def dfs(eid):
            employee = emap[eid]
            return (employee.importance +
                    sum(dfs(eid) for eid in employee.subordinates))
        return dfs(query_id)

    def getImportance(self, employees, id):
        from collections import deque
        e = {e.id: e for e in employees}
        q = deque([id])
        res = 0
        while q:
            _id = q.popleft()
            res += e[_id].importance
            q += [employee_id for employee_id in e[_id].subordinates]
        return res

