class Solution(object):
    def plusOne(self, digits):
        for index in reversed(range(len(digits))):
            if digits[index] < 9:
                digits[index] += 1
                return digits
            else:
                digits[index] = 0
        digits.insert(0, 1)
        return digits

