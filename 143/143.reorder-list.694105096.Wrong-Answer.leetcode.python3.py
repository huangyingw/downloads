class Solution(object):
    def reorderList(self, head):
        def split(head):
            slow = fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            print("slow --> %s" % slow.val)
            mid = slow
            print("mid --> %s" % mid.val)
            slow.next = None
            return mid

        def reverse(head):
            pre = None
            while head:
                print("head --> %s" % head.val)
                nex = head.next
                head.next = pre
                pre = head
                head = nex
            if pre:
                print("pre --> %s" % pre.val)
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
        mid = reverse(mid)
        temp = mid
        while temp:
            print("%s, " % temp.val)
            temp = temp.next
        merge(head, mid)

