class Solution(object):
    def swapPairs(self, head):
        if not head:
            return head
        ref = head
        while ref and ref.next:
            ref.val, ref.next.val = ref.next.val, ref.val
            ref = ref.next.next
        return head

