import collections


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        dish = set()
        table = collections.defaultdict(collections.Counter)
        for order in orders:
            table[order[1]][order[2]] += 1
            dish.add(order[2])
        res = []
        dish = sorted(list(dish))
        res.append(["Table"])
        for d in dish:
            res[0].append(d)
        for key in sorted(table.keys(), key=int):
            res.append([key] + [str(table[key][food]) for food in dish])
        return res

