class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        def transform(x):
            return a * x * x + b * x + c
        transformed = [transform(num) for num in nums]
        left, right = 0, len(nums)
        result = []
        while left < right:
            if (a > 0 and transformed[left] > transformed[right]) or (a <= 0 and transformed[right] > transformed[left]):
                result.append(transformed[left])
                left += 1
            else:
                result.append(transformed[right])
        return result[::-1] if a > 0 else result

