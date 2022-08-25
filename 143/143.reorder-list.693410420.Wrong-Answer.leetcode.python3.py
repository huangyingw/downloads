class Solution(object):
    def reorderList(self, head):
        def split(head):
            dummy = ListNode(-1)
            dummy.next = head
            slow = fast = dummy
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            print("slow --> %s" % slow.val)
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
            while l1 and l2:
                nav.next = l1
                l1 = l1.next
                nav = nav.next
                nav.next = l2
                l2 = l2.next
        mid = split(head)
        print("mid --> %s" % mid.val)
        reverse(mid)
        merge(head, mid)

