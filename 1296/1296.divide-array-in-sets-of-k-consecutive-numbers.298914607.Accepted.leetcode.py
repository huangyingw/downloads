class Solution(object):
    def isPossibleDivide(self, nums, k):

        from collections import Counter
        count_map = Counter(nums)
        for num in sorted(count_map.keys()):
            if count_map[num] <= 0:
                continue
            for index in range(1, k):
                count_map[num + index] -= count_map[num]
                if count_map[num + index] < 0:
                    return False
        return True

