class Solution(object):
    def isPalindrome(self, head):
        rev = None
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            temp = slow
            print("temp --> %s" % temp.val)
            slow = slow.next
            print("slow --> %s" % slow.val)
            temp.next = rev
            rev = temp
            print("rev --> %s" % rev.val)
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            rev = rev.next
            slow = slow.next
        return not rev

