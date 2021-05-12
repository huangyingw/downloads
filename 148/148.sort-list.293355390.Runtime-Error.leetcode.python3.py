class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head
        fast, slow, prev = head, head, None
        while fast and fast.next:
            prev, slow, fast = slow, slow.next, fast.next.next
        prev.next = None
        one = self.sortList(head)
        two = self.sortList(slow)
        return self.merge(one, two)

    def merge(self, one, two):
        dummy = merged = ListNode()
        while one and two:
            if one.val <= two.val:
                merged.next = one
                one = one.next
            else:
                merged.next = two
                two = two.next
            merged = merged.next
        merged.next = one or two
        return dummy.next

