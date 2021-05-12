class Solution(object):
    def sumOfDigits(self, A):
        minimum = min(A)
        digit_sum = 0
        while minimum:
            digit_sum += minimum % 10
            minimum /= 10
        return int(digit_sum % 2 == 0)

