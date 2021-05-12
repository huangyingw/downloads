class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        rest = 0
        for num in nums:
            rest ^= num
        return rest

