class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        priorityQueue = []
        res = []
        if not k or not nums1 or not nums2:
            return res
        for i in range(min(len(nums1), k)):
            heapq.heappush(priorityQueue, (nums1[i] + nums2[0], i, 0))
        while k > 0 and priorityQueue:
            k -= 1
            _, i, j = heapq.heappop(priorityQueue)
            res.append([nums1[i], nums2[j]])
            if j < len(nums2) - 1:
                heapq.heappush(priorityQueue, (nums1[i] + nums2[j + 1], i, j + 1))
        return res

