class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        if not target:
            return []
        res = []

        index = 0
        for i in range(1, target[-1] + 1):
            if target[index] == i:
                res.append("Push")
                index += 1
            else:
                res += ["Push", "Pop"]

        return res

