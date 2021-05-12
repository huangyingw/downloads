class Solution:
    def maximum69Number(self, num: int) -> int:
        six_index, i, temp = -1, 0, num
        while temp > 0:
            if temp % 10 == 6:
                six_index = i
            temp //= 10
            i += 1
        return (num + 3 * (10**six_index)) if six_index != -1 else num

