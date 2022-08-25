class Solution(object):
    def reverseList(self, head):
        prev = None
        while prev:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        print("prev --> %s" % prev.val)
        return prev

