class Solution(object):
    def reverseList(self, head):
        pre = None
        while head:
            temp = head.next
            head.next = pre
            pre = head
            head = temp
        return pre

    def isPalindrome(self, head):
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        end = self.reverseList(slow)
        while head and end:
            if head.val != end.val:
                return False
            head = head.next
            end = end.next
        return True

