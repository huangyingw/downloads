class Solution:
    def getMinimumDifference(self, root):
        iot_list = []

        def InOrderTraversal(node):
            if node.left:
                InOrderTraversal(node.left)
            iot_list.append(node.val)
            if node.right:
                InOrderTraversal(node.right)
            return
        InOrderTraversal(root)
        min_abs = float('inf')
        for i in range(1, len(iot_list)):
            diff = iot_list[i] - iot_list[i - 1]
            if diff < min_abs:
                min_abs = diff
        return min_abs

