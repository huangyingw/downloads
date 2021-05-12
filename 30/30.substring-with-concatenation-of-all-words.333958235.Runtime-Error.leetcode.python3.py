class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        return self.dfs(root, arr, 0)

    def dfs(self, root: TreeNode, arr: List[int], Index: int) -> bool:

        if Index >= len(arr):
            return False

        elif (root.left == None) and (root.right == None) and (root.val == arr[Index]) and (Index + 1 == len(arr)):
            return True

        elif (root.right == None) and (root.left == None):
            return False
        elif root.left == None:
            return (root.val == arr[Index]) and (self.dfs(root.right, arr, Index + 1))
        elif root.right == None:
            return (root.val == arr[Index]) and (self.dfs(root.left, arr, Index + 1))

        return (root.val == arr[Index]) and (self.dfs(root.left, arr, Index + 1) or self.dfs(root.right, arr, Index + 1))

