class Solution(object):
    def reverseList(self, head):
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
            print("head --> %s" % head.val)
        return prev

