class Solution:
    def connect(self, root):
        if root:
            p = root
            q = None
            nextNode = None
            while p:
                if p.left:
                    if q:
                        q.next = p.left
                    q = p.left
                    if nextNode == None:
                        nextNode = q
                if p.right:
                    if q:
                        q.next = p.right
                    q = p.right
                    if nextNode == None:
                        nextNode = q
                p = p.next
            self.connect(nextNode)

