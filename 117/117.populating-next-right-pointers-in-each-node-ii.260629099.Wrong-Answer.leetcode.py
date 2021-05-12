class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root:
            return
        queue = collections.deque()
        queue.append(root)
        while len(queue) > 0:
            size = len(queue)
            prev = None
            for i in range(size):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                if i == 0:
                    prev = cur
                else:
                    prev.next = cur
                    prev = cur

