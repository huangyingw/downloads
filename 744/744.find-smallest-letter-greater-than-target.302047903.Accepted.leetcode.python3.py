class Solution:
    def nextGreatestLetter(self, letters, target):
        if ord(target) >= ord(letters[-1]):
            return letters[0]
        start, last = 0, len(letters) - 1
        while start <= last:
            mid = (start + last) // 2
            if letters[mid] > target:
                last = mid - 1
            else:
                start = mid + 1
        return letters[start]

