class Solution(object):
    def isHappy(self, n):
        def calculateSum(n):
            sum = 0
            while n:
                tmp = n % 10
                sum += tmp * tmp
                n //= 10
            return sum
        slow = fast = n
        while True:
            slow = calculateSum(slow)
            fast = calculateSum(fast)
            fast = calculateSum(fast)
            if slow == fast:
                break
        return slow == 1

