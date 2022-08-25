class Solution(object):
    def subarraySum(self, nums, k):
        count, summ, d = 0, 0, {0: 1}
        for n in nums:
            summ += n
            if summ - k in d:
                count += d[summ - k]
            d[summ] = d.setdefault(summ, 0) + 1
        return count

