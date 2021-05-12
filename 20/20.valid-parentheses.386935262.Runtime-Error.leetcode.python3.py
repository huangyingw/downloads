class Solution:
    def reorderList(self, head: ListNode) -> None:

        if (head == None or head.next == None or head.next.next == None):
            return
        else:
            fast, slow = head, head

            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next

            Second = slow.next
            pre = None
            slow.next = None
            while Second:
                nextN = Second.next
                Second.next = pre
                pre = Second
                Second = nextN

            while pre:
                nextN = pre
                pre = pre.next
                nextN.next = head.next
                head.next = nextN
                head = head.next.next

