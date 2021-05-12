class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        q = [[root]]
        for level in q:
            record = []
            for node in level:
                if node.left:
                    record += [node.left]
                if node.right:
                    record += [node.right]
            if record:
                q += [record]
        return [[x.val for x in level] for level in q]

