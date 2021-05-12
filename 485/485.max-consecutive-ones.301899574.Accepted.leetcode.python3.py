class Solution:
    def findMaxConsecutiveOnes(self, nums):
        temp = bytearray(nums).split(b'\x00')
        return max([len(i) for i in temp])

