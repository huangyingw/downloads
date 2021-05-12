class Solution(object):
    def isPalindrome(self, head):
        rev = None
        slow, fast = head, head
        while slow and slow.next:
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while rev and slow and rev.val == slow.val:
            rev = rev.next
            slow = slow.next
        return not rev

