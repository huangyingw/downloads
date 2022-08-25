class Solution:
    def twoSum(self, numbers, target):
        pair = {}
        for i in range(len(numbers)):
            if numbers[i] in pair.keys():
                return [pair.get(numbers[i]), i + 1]
            else:
                pair[target - numbers[i]] = i + 1

