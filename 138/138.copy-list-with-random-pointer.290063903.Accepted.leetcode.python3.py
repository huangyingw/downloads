class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        cur = head
        while cur:
            new_node = Node(cur.val)
            cur.next, new_node.next = new_node, cur.next
            cur = new_node.next
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        cur = head
        dummyHead = Node(0)
        newCur = dummyHead
        while cur:
            newCur.next = cur.next
            cur = cur.next.next
            newCur = newCur.next
        return dummyHead.next

