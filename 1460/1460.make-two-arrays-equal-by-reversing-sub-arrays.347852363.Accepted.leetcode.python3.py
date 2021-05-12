class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if len(target) != len(arr):
            return False
        d = {}
        for i in range(len(arr)):
            d[arr[i]] = d.get(arr[i], 0) + 1
            d[target[i]] = d.get(target[i], 0) - 1

        for value in d.values():
            if value != 0:
                return False
        return True

