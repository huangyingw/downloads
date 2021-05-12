class Solution:
    def findRestaurant(self, list1, list2):
        common = set(list1) & set(list2)
        index_sum = 0
        res = []
        for i in common:
            index_sum = list1.index(i) + list2.index(i)
            res.append((index_sum, list1.index(i)))
        res.sort()
        ret = []
        sum_index = res[0][0]
        for i in res:
            if i[0] == sum_index:
                ret.append(list1[i[1]])
        return ret

