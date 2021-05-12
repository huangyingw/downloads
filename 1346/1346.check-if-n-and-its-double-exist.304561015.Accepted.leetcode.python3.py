class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        visited = set()
        for no in arr:
            if no / 2 in visited or no + no in visited:
                return True
            visited.add(no)
        return False

