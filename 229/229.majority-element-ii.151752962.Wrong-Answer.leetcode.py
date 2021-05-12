class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):
        n1 = n2 = None
        c1 = c2 = 0
        for num in nums:
            if n1 == num:
                c1 += 1
            elif n2 == num:
                c2 += 1
            elif c1 > c2:
                n2, c2 = (n2, c2 - 1) if c2 > 1 else (num, 1)
            else:
                n1, c1 = (n1, c1 - 1) if c1 > 1 else (num, 1)
        ans, size = [], len(nums)
        if n1 is not None and sum([x == n1 for x in nums]) > size / 3:
            ans.append(n1)
        if n2 is not None and sum([x == n2 for x in nums]) > size / 3:
            ans.append(n2)
        return sorted(ans)

