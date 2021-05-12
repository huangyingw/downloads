class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        start = 0
        end = len(nums1)
        while start <= end:
            midX = (start + end) // 2
            midY = ((len(nums1) + len(nums2) + 1) // 2) - midX
            leftX = float('-inf') if midX == 0 else nums1[midX - 1]
            rightX = float('inf') if midX == len(nums1) else nums1[midX]

            leftY = float('-inf') if midY == 0 else nums2[midY - 1]
            rightY = float('inf') if midY == len(nums2) else nums2[midY]
            if leftX <= rightY and leftY <= rightX:
                if (len(nums1) + len(nums2)) % 2 == 0:
                    return (max(leftX, leftY) + min(rightX, rightY)) / 2
                else:
                    return max(leftX, leftY)

            elif leftX > rightY:
                end = midX - 1
            else:
                start = midX + 1

