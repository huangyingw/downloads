class Solution(object):
    def detectCycle(self, head):
        if not head:
            return None
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        print("slow 1 --> %s" % slow.val)
        print("fast --> %s" % fast.val)
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            print("slow 2 --> %s" % slow.val)
            return slow
        return None

