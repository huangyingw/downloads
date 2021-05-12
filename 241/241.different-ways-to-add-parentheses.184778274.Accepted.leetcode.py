class Solution(object):
    def diffWaysToCompute(self, input):
        result = []

        for idx, val in enumerate(input):
            if val == '+' or val == '-' or val == '*':
                left = self.diffWaysToCompute(input[: idx])
                right = self.diffWaysToCompute(input[idx + 1:])

                for l in left:
                    for r in right:
                        if val == '+':
                            result.append(l + r)
                        elif val == '-':
                            result.append(l - r)
                        elif val == '*':
                            result.append(l * r)

        if input.isdigit():
            result.append(int(input))

        return result

