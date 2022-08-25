class Solution(object):
    def reorderList(self, head):
        def split(head):
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            mid = slow.next
            slow.next = None
            return mid

        def reverse(head):
            pre = None
            while head:
                temp = head.next
                head.next = pre
                pre = head
                head = temp
            return pre

        def merge(l1, l2):
            dummy = ListNode(-1)
            nav = dummy
            while l2:
                nav.next = l1
                nav = nav.next
                nav.next = l2
                nav = nav.next
                l1 = l1.next
                l2 = l2.next
        mid = split(head)
        reverse(mid)
        merge(head, mid)

