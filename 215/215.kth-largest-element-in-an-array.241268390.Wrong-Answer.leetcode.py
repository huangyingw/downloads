class Solution(object):
    def findKthLargest(self, nums, k):
        def partition(start, end):
            pivot = nums[start]
            left = start + 1
            right = end

            while left < right:
                if nums[left] >= pivot:
                    left += 1
                    print('left nums[%s] --> %s' % (left, nums[left]))
                elif nums[right] <= pivot:
                    right -= 1
                    print('right nums[%s] --> %s' % (right, nums[right]))
                else:
                    nums[left], nums[right] = nums[right], nums[left]
                    print('swap (%s, %s)' % (nums[left], nums[right]))

            nums[start] = nums[right]
            nums[right] = pivot
            return right

        def select(left, right):
            print('nums before --> %s' % nums)
            pivot = partition(left, right)
            print('pivot --> %s' % nums[pivot])
            print('nums after --> %s' % nums)

            if pivot + 1 == k:
                return nums[pivot]
            elif pivot + 1 > k:
                return select(left, pivot - 1)
            else:
                return select(pivot + 1, right)

        return select(0, len(nums) - 1)

