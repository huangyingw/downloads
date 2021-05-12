class Solution:
    def binaryTreePaths(self, root):
        def searchBT(root, path, ans):
            if root.left == None and root.right == None:
                ans.append(path + str(root.val))
            if root.left:
                searchBT(root.left, path + str(root.val) + "->", ans)
            if root.right:
                searchBT(root.right, path + str(root.val) + "->", ans)
        ans = []
        if root:
            searchBT(root, "", ans)
        return ans

