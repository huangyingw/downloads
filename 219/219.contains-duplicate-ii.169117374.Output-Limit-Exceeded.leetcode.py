class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        val_idx = {}

        for idx, val in enumerate(nums):
            print('idx --> %s' % idx)
            print('val --> %s' % val)

            if val not in val_idx:
                val_idx[val] = idx
            elif abs(val_idx[val] - idx) <= k:
                return True
            else:
                val_idx[val] = idx

        return False

