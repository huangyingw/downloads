class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for no in nums:
            xor ^= no
        res = [0, 0]
        xor &= -xor
        for no in nums:
            if xor & no == 0:
                res[0] ^= no
            else:
                res[1] ^= no
        return res

