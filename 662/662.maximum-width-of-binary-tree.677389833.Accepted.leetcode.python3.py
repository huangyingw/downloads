class Solution(object):
    def widthOfBinaryTree(self, root):
        if not root:
            return 0
        max_width = 1
        nodes = [(root, 0)]
        while True:
            new_nodes = []
            for node, i in nodes:
                if node.left:
                    new_nodes.append((node.left, i * 2))
                if node.right:
                    new_nodes.append((node.right, i * 2 + 1))
            if not new_nodes:
                break
            nodes = new_nodes
            max_width = max(max_width, 1 + nodes[-1][1] - nodes[0][1])
        return max_width

