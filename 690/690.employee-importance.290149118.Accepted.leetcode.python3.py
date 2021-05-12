class Solution:
    def getImportance(self, employees, id):
        pending = [id]
        imp = 0
        while pending:
            pending, imp = self.processing(employees, pending, imp)
        return imp

    def processing(self, employees, pending, imp):
        tmp = []
        for n in range(len(employees)):
            if employees[n].id in pending:
                imp += employees[n].importance
                tmp += employees[n].subordinates
        return tmp, imp

