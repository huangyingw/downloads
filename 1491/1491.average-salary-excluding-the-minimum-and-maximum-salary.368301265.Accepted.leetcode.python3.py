class Solution:
    def average(self, salary: List[int]) -> float:
        max_salary, min_salary, salary_sum = -1, float('inf'), 0

        for sal in salary:
            salary_sum += sal
            if sal < min_salary:
                min_salary = sal
            if sal > max_salary:
                max_salary = sal

        return (salary_sum - (min_salary + max_salary)) / (len(salary) - 2)

