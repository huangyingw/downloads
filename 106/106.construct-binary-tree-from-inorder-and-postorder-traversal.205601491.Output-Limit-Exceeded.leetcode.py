class Solution(object):
    def buildTree(self, inorder, postorder):
        inv_map = {v: k for k, v in enumerate(inorder)}
        return self.dfs(inv_map, inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1)

    def dfs(self, inv_map, inorder, inLeft, inRight, postorder, poLeft, poRight):
        print("poRight --> %s" % poRight)
        print("postorder[poRight] --> %s" % postorder[poRight])
        mid = inv_map[postorder[poRight]]
        print("mid --> %s" % mid)
        root = TreeNode(inorder[mid])
        root.left = self.dfs(inv_map, inorder, inLeft, mid - 1, postorder, poLeft, poLeft + mid - 1 - inLeft)
        root.right = self.dfs(inv_map, inorder, mid + 1, inRight, postorder, mid - inRight + poRight, poRight - 1)
        return root

