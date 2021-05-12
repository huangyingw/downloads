class Solution:
    def maxDiff(self, num: int) -> int:
        num = list(str(num))
        first_digit = num[0]
        x = '9'
        y = num[0] if num[0] != '1' else '0'

        for i in num:
            if i != x:
                x = i
                break

        if y == '0':
            for i in range(1, len(num)):
                if num[i] not in ['0', '1']:
                    y = num[i]
                    break

        num1 = [i for i in num]
        for i in range(len(num)):
            if num[i] == x:
                num[i] = '9'
            if num1[i] == y:
                num1[i] = '1' if first_digit != '1' else '0'

        return int("".join(num)) - int("".join(num1))

