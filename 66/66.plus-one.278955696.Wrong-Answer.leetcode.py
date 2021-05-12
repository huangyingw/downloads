class Solution(object):
    def plusOne(self, digits):
        for index in reversed(range(len(digits))):
            digits[index] += 1
            if digits[index] < 9:
                return digits
            else:
                digits[index] = 0
        digits.insert(0, 1)
        return digits

