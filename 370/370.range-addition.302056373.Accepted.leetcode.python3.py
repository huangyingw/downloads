class Solution(object):
    def getModifiedArray(self, length, updates):
        shifts = [0] * (length + 1)
        for start, end, inc in updates:
            shifts[start] += inc
            shifts[end + 1] -= inc
        output = [shifts[0]]
        for i in range(1, length):
            output.append(output[-1] + shifts[i])
        return output

