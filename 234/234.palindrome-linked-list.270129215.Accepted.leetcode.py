class Solution(object):
    def isPalindrome(self, head):
        if not head:
            return True
        p1, p2 = head, head
        p3, pre = p1.next, p1
        while p2.next and p2.next.next:
            p2 = p2.next.next
            pre = p1
            p1 = p3
            p3 = p3.next
            p1.next = pre
        if not p2.next:
            p1 = p1.next
        while p3:
            if p1.val != p3.val:
                return False
            p1 = p1.next
            p3 = p3.next
        return True

