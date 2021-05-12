class Solution(object):
    def plusOne(self, head):
        new_head = ListNode(0)
        new_head.next = head
        i, j = new_head, new_head
        while i.next:
            i = i.next
            if i.val != 9:
                j = i
        j.val += 1
        j = j.next
        while j:
            j.val = 0
            j = j.next
        if new_head.val == 0:
            return head
        return new_head

