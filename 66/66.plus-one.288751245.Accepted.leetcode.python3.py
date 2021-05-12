class Solution(object):
    def plusOne(self, digits):
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1
            if digits[i] > 9:
                digits[i] = 0
            else:
                return digits
        digits.insert(0, 1)
        return digits

