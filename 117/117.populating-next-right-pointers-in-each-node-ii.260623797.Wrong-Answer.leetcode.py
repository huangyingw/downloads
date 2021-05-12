class Solution:
    def connect(self, root):
        head = root
        while head:
            next_head = None
            for node in Solution.getLinkedList(head):
                if not next_head:
                    next_head = cur = node
                else:
                    cur.next = cur = node
            head = next_head

    @staticmethod
    def getLinkedList(head):
        while head:
            for node in head.left, head.right:
                if node:
                    yield node
            head = head.next

