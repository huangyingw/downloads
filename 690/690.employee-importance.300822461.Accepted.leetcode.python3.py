class Solution(object):
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

