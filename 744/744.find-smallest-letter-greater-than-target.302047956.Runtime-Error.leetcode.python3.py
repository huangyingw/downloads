class Solution:
    def nextGreatestLetter(self, letters, target):
        start, last = 0, len(letters) - 1
        while start <= last:
            mid = (start + last) // 2
            if letters[mid] > target:
                last = mid - 1
            else:
                start = mid + 1
        return letters[start]

