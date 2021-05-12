class Solution1:
    def middleNode(self, head: ListNode) -> ListNode:
        ll = []

        while(head):
            ll.append(head)
            head = head.next

        return ll[(len(ll)) // 2]


class Solution2:
    def middleNode(self, head: ListNode) -> ListNode:
        fast = slow = head

        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next

        return slow

