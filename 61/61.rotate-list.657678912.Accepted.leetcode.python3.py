class Solution(object):
    def rotateRight(self, head, k):
        if not head:
            return
        l = self.length(head)
        k = k % l
        if l == 1 or k % l == 0:
            return head
        count = 0
        curr = head
        while count < l - k:
            prev = head
            head = head.next
            count += 1
        prev.next = None
        result = head
        while head.next:
            head = head.next
        head.next = curr
        return result

    def length(self, head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count

