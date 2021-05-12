class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = []
        values = [a, b, c]
        old_values = [a, b, c]
        max_value = max(values)
        index = values.index(max_value)

        while max_value:
            if max_value >= 2 and (max(old_values) - max_value <= 2):
                old_values = [value for value in values]
                res.append(chr(index + ord('a')) * 2)
                values[index] -= 2
            else:
                old_values = [value for value in values]
                res.append(chr(index + ord('a')))
                values[index] -= 1

            if index == 0:
                max_value = values[1] if values[1] > values[2] else values[2]
                index = 1 if values[1] > values[2] else 2
            elif index == 1:
                max_value = values[0] if values[0] > values[2] else values[2]
                index = 0 if values[0] > values[2] else 2
            else:
                max_value = values[0] if values[0] > values[1] else values[1]
                index = 0 if values[0] > values[1] else 1

        return "".join(res)

