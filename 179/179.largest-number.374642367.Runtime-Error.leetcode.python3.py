from functools import cmp_to_key


class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution1:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num


class Solution2:
	def largestNumber(self, A):

	    A = map(str, A)
     key = cmp_to_key(lambda a,b: 1 if a+b >= b+a else -1)
     res = ''.join(sorted(A, key= key, reverse=True))
     
     res = res.lstrip('0')
     return res if res else '0'
class Solution:
    def largestNumber(self, nums):
        nums = self.mergeSort(nums, 0, len(nums)-1)
        return str(int("".join(map(str, nums))))
    
    def mergeSort(self, nums, l, r):
        if l > r:
            return 
        if l == r:
            return [nums[l]]
        mid = l + (r-l)//2
        left = self.mergeSort(nums, l, mid)
        right = self.mergeSort(nums, mid+1, r)
        return self.merge(left, right)
    def merge(self, l1, l2):
        res, i, j = [], 0, 0
        while i < len(l1) and j < len(l2):
            if not self.compare(l1[i], l2[j]):
                res.append(l2[j])
                j += 1
            else:
                res.append(l1[i])
                i += 1
        res.extend(l1[i:] or l2[j:])
        return res
    
    def compare(self, n1, n2):
        return str(n1) + str(n2) > str(n2) + str(n1)

