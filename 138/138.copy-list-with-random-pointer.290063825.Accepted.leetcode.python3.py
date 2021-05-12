class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        clone_map = {}
        cur = head
        while cur:
            clone_map[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            clone_map.get(cur).next = clone_map.get(cur.next)
            clone_map.get(cur).random = clone_map.get(cur.random)
            cur = cur.next
        return clone_map.get(head)

