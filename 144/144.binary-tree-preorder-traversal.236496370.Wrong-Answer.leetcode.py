class Solution(object):
    def preorderTraversal(self, root):
        result = []
        stack = [root]

        while stack and root:
            print('root 1 --> %s' % root.val)
            if root:
                print('root 2 --> %s' % root.val)
                result.append(root.val)
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                print('root 3 --> %s' % root.val)
                root = root.right
        return result

