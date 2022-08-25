class Solution(object):
    def isPalindrome(self, head):
        rev = None
        slow, fast = head, head
        while slow:
            rev, rev.next, slow = slow, rev, slow.next
        while rev and slow and rev.val == slow.val:
            rev = rev.next
            slow = slow.next
        return not rev

