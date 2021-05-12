from collections import Counter, defaultdict


class Solution(object):
    def topKFrequent(self, nums, k):
        counter = defaultdict(list)
        for key, val in Counter(nums).items():
            counter[val].append(key)
        result = []
        for i in reversed(range(len(nums))):
            result.extend(counter[i])
            if len(result) >= k:
                return result[:k]
        return result[:k]

