class Solution(object):
    def copyRandomList(self, head):
        p = head
        while p:
            next = p.next
            copy = Node(p.val, None, None)
            p.next = copy
            copy.next = next
            p = next
        p = head
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next
        p = head
        if p:
            headCopy = p.next
        else:
            headCopy = None
        while p:
            copy = p.next
            p.next = copy.next
            p = p.next
            if p:
                copy.next = p.next
        return headCopy

