class Solution(object):
    def rotateRight(self, head, k):
        if k == 0:
            return head
        if not head:
            return None
        tempHead, length = head, 1
        while tempHead.next:
            length += 1
            tempHead = tempHead.next
        tempHead.next = head
        jump = (length - k) % length
        previous = tempHead
        while jump > 0:
            previous = previous.next
            jump -= 1
        head = previous.next
        previous.next = None
        return head

