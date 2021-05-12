class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = {}
        for number in arr:
            count[number] = count.get(number, 0) + 1

        res = -1
        for key, value in count.items():
            if key == value and key > res:
                res = key
        return res

