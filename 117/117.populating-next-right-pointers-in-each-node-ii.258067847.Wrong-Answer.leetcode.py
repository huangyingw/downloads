class Solution:
    def connect(self, root):
        if not root:
            return
        queue = collections.deque()
        queue.append(root)
        while queue:
            _len = len(queue)
            for i in range(_len):
                node = queue.popleft()
                if i < _len - 1:
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

