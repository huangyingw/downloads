class Solution(object):
    def nextGreatestLetter(self, letters, target):
        left, right = 0, len(letters)
        while left < right:
            mid = (left + right) // 2
            if target >= letters[mid]:
                left = mid + 1
            else:
                right = mid
        return letters[left]

