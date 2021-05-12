class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        for x in range(int((num + 2)**0.5), 0, -1):
            if (num + 1) % x == 0:
                return [x, (num + 1) // x]
            elif (num + 2) % x == 0:
                return [x, (num + 2) // x]


"""
The reason for doing it from sqrt is that the factors start repeating in the reverse 
order after the square root.
eg: 100
The table produced is:
1*100    ^
2*50     |
4*25     |
5*20     |  (Increasing distance as we go up)
10*10 <- sqrt, we see repetitions after this point (Also notice this is the closest)
20*5 
25*4 
2*50 
100*1
"""

