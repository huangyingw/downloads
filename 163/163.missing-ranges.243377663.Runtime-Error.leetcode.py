class Solution(object):
    def missingRange(self, A, lower, upper):
        if not A:
            return []
        result = []
        if A[0] != lower:
            end = A[0] - 1
            if end == lower:
                m_r = str(lower)
            else:
                m_r = str(lower) + "->" + str(end)
            result.append(m_r)
        for index in range(1, len(A)):
            if A[index] != A[index - 1] + 1:
                start = A[index - 1] + 1
                end = A[index] - 1
                if start == end:
                    m_r = str(start)
                else:
                    m_r = str(start) + "->" + str(end)
                result.append(m_r)
        if A[len(A) - 1] != upper:
            start = A[len(A) - 1] + 1
            if start == upper:
                m_r = str(start)
            else:
                m_r = str(start) + "->" + str(upper)
            result.append(m_r)
        return result

