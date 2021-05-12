class Solution:

    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack, res = [], [-1] * len(nums)
        for i in range(2 * len(nums) - 1, -1, -1):
            index = i % len(nums)
            while stack and nums[stack[-1]] <= nums[index]:
                stack.pop()

            res[index] = nums[stack[-1]] if stack else -1
            stack.append(index)
        return res

