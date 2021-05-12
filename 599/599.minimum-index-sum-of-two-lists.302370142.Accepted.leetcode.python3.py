class Solution:
    def findRestaurant(self, list1, list2):
        d = {}
        for i, r in enumerate(list1):
            d[r] = i
        res = []
        imin = len(list1) + len(list2)
        for i, r in enumerate(list2):
            if r in d and d[r] + i <= imin:
                if d[r] + i == imin:
                    res.append(r)
                else:
                    res = []
                    res.append(r)
                    imin = d[r] + i
        return res

