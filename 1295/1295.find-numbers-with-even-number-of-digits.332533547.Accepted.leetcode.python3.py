class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(self.number_of_digits(number) for number in nums)

    def number_of_digits(self, n):
        count = 0
        while n:
            count += 1
            n //= 10
        return 1 if count % 2 == 0 else 0

