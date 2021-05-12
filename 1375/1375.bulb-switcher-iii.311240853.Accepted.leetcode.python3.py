class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        cur_sum = max_sum = count = 0
        max_value = -1
        for pos in light:
            cur_sum += pos
            if max_value < pos:
                max_value = pos
                max_sum = (pos * (pos + 1)) // 2
            if cur_sum == max_sum:
                count += 1
        return count


class Solution1:
    def numTimesAllBlue(self, A):
        right = res = 0
        for i, a in enumerate(A, 1):
            right = max(right, a)
            res += right == i
        return res

