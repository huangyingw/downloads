class Solution(object):
    def getImportance(self, employees, id):
        importance, subordinates, sum_importances = {}, {}, {}
        for employee in employees:
            importance[employee.id] = employee.importance
            subordinates[employee.id] = employee.subordinates

        def sum_importance(emp_id):
            if emp_id in sum_importances:
                return sum_importances[emp_id]
            total = importance[emp_id]
            for sub in subordinates[emp_id]:
                total += sum_importance(sub)
            sum_importances[emp_id] = total
            return total
        return sum_importance(id)

