from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks).values()
        M = max(task_counts)
        m_count = 0
        for i in task_counts:
            if i == M:
                m_count += 1
        return max(len(tasks), (M - 1) * (n + 1) + m_count)

