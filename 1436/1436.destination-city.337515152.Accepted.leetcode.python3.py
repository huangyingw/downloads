class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        temp = set()
        res = set()

        for path in paths:
            temp.add(path[0])
            if path[0] in res:
                res.remove(path[0])

            if path[1] not in temp:
                res.add(path[1])
        return res.pop()

