class Solution(object):
    def hasCycle(self, head):
        slow = fast = head
        try:
            while True:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return True
        except:
            return False

