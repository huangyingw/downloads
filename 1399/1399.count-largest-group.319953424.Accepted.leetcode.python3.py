class Solution:
    def countLargestGroup(self, n: int) -> int:
        d = {}
        max_value = count = 0
        for number in range(1, n + 1):
            num_sum = self.number_sum(number)
            d[num_sum] = d.get(num_sum, 0) + 1

            if d[num_sum] > max_value:
                count = 0
                max_value = d[num_sum]

            if d[num_sum] == max_value:
                count += 1
        return count

    def number_sum(self, n):
        num_sum = 0
        while n:
            num_sum += n % 10
            n //= 10
        return num_sum

