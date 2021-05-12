class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        val_idx = {}

        for idx, val in enumerate(nums):
            if val not in val_idx:
                val_idx[val] = idx
            elif abs(val_idx[val] - idx) <= k:
                return True

        return False

