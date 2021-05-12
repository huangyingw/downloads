class Solution(object):
    def swapPairs(self, head):
        if not head:
            return None
        cur = head.next if head.next else head
        prev = None
        while head and head.next:
            temp = head.next
            head.next = head.next.next
            temp.next = head
            head = head.next
            if prev:
                prev.next = temp
            prev = temp.next
        return cur

