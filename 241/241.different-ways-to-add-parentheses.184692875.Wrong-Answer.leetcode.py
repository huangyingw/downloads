class Solution(object):
    def diffWaysToCompute(self, input):
        result = []

        for idx, val in enumerate(input):
            print 'val --> ' + str(val)
            if val == '+' or val == '-' or val == '*':
                left = self.diffWaysToCompute(input[: idx])
                print 'left --> ' + str(left)
                right = self.diffWaysToCompute(input[idx + 1:])
                print 'right --> ' + str(right)

                for l in left:
                    for r in right:
                        if val == '+':
                            result.append(l + r)
                        elif val == '-':
                            result.append(l - r)
                        elif val == '*':
                            result.append(l + r)

        if input.isdigit():
            result.append(int(input))

        print 'result --> ' + str(result)
        return result

