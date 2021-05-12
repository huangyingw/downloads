class Solution(object):
    def reverse(self, head):
        pre = None
        temp = None
        current = head

        while current:
            temp = current.next
            current.next = pre
            pre = current
            current = temp
        return pre

    def split(self, head):
        lists = [None for _ in range(2)]
        lists[0] = head

        if not head or not head.next:
            return lists

        slow = head
        fast = head.next.next

        while fast:
            slow = slow.next

            if not fast.next:
                break
            fast = fast.next.next
        lists[1] = slow.next
        slow.next = None
        return lists

    def merge(self, l1, l2):

        while l2:
            temp = l1.next
            l1.next = l2
            l1 = temp
            temp = l2.next
            l2.next = l1
            l2 = temp

    def reorderList(self, head):
        lists = self.split(head)
        lists[1] = self.reverse(lists[1])
        self.merge(lists[0], lists[1])

