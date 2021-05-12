class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None
        p = head
        while p:
            newP = Node(p.val)
            newP.next = p.next
            newP.random = p.random
            p.next = newP
            p = newP.next
        p = head
        newHead = p.next
        while p:
            newP = p.next
            if newP.random:
                newP.random = newP.random.next
            p = newP.next
        p = head
        while p:
            newP = p.next
            p.next = newP.next
            if newP.next:
                newP.next = newP.next.next
            p = p.next
        return newHead

