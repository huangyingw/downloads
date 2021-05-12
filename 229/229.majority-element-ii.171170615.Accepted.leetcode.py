class Solution:
    def majorityElement(self, nums):
        n1 = n2 = None
        c1 = c2 = 0

        for num in nums:
            if n1 == num:
                c1 += 1
            elif n2 == num:
                c2 += 1
            elif c1 == 0:
                n1, c1 = num, 1
            elif c2 == 0:
                n2, c2 = num, 1
            else:
                c1 -= 1
                c2 -= 1

        ans, size = [], len(nums)

        if n1 is not None and sum([x == n1 for x in nums]) > size / 3:
            ans.append(n1)

        if n2 is not None and sum([x == n2 for x in nums]) > size / 3:
            ans.append(n2)

        return sorted(ans)

