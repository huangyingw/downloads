"""
Problem Link: https://leetcode.com/problems/intersection-of-two-arrays-ii/

Given two arrays, write a function to compute their intersection.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.

Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements 
into the memory at once?
"""
class Solution:
    # Time Complexity - O(m+n)
    # Space Complexity - O(min(m,n))
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums2) > len(nums1):
          # it will reduce the space complexity to O(min(m,n)) 
          self.intersect(nums2, nums1)
        
        d = {}
        res = []
        for no in nums1:
          d[no] = d.get(no,0) + 1
        
        for no in nums2:
          if no in d and d[no]:
            res.append(no)
            d[no] -= 1
        return res

# Follow Up - 1
class Solution:
    # Time Complexity - O(m+n), by assuming arrays are already sorted
    # Space Complexity - O(1)
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums2) > len(nums1):
          self.intersect(nums2, nums1)
        
        nums1.sort()
        nums2.sort()
        p1 = p2 = 0
        res = []
        while p1 < len(nums1) and p2 < len(nums2):
          if nums1[p1] == nums2[p2]:
            res.append(nums1[p1])
            p1 += 1
            p2 += 1
          elif nums1[p1] < nums2[p2]:
            p1 += 1
          else:
            p2 += 1
        return res

# Follow Up - 3
"""
What if elements of nums2 are stored on disk, and the memory is
limited such that you cannot load all elements into the memory at
once?

If only nums2 cannot fit in memory, put all elements of nums1 into a HashMap, 
read chunks of array that fit into the memory, and record the intersections.
If both nums1 and nums2 are so huge that neither fit into the memory, 
sort them individually (external sort), then read 2 elements from each 
array at a time in memory, record intersections.
"""
