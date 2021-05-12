class Solution:
    def isValidBST(self, root):
        stack, prev, curr = [root], None, root
        while stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            top = stack.pop()
            if prev and prev.val >= top.val:
                return False
            prev = top
            curr = top.right
        return True

