class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, summ, d = 0, 0, {0: 1}
        for n in nums:
            summ += n
            if summ - k in d:
                count += d[summ - k]
            d[summ] = d.get(summ, 0) + 1
        return count

