class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        x, y = len(nums1), len(nums2)
        low, high = 0, x
        while low <= high:
            partitionx = (low + high) / 2
            partitiony = (x + y + 1) / 2 - partitionx
            if partitionx == 0:
                maxLeftX = float('-inf')
            else:
                maxLeftX = nums1[partitionx - 1]
            if partitionx == x:
                minRightX = float('inf')
            else:
                minRightX = nums1[partitionx]
            if partitiony == 0:
                maxLeftY = float('-inf')
            else:
                maxLeftY = nums2[partitiony - 1]
            if partitiony == y:
                minRightY = float('inf')
            else:
                minRightY = nums2[partitiony]
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if((x + y) % 2 == 0):
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
                else:
                    return max(maxLeftY, maxLeftX)
            elif maxLeftX > minRightY:
                high = partitionx - 1
            else:
                low = partitionx + 1

