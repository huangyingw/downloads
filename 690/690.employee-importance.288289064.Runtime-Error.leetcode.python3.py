class Solution(object):
    def getImportance(self, employees, id):
        importance, subordinates, sum_importance = {}, {}, {}
        for employee in employees:
            importance[employee.id] = employee.importance
            subordinates[employee.id] = employee.subordinates

        def sum_importance(emp_id):
            if emp_id in sum_importance:
                return sum_importance[emp_id]
            total = importance[emp_id]
            for sub in subordinates[emp_id]:
                total += sum_importance(sub)
            sum_importance[emp_id] = total
            return total
        return sum_importance(id)

