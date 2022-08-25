class Solution(object):
    def reorderList(self, head):
        def split(head):
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            result = slow.next
            slow.next = None
            return result

        def reverse(head):
            pre = None
            while head:
                temp = head.next
                head.next = pre
                pre = head
                head = temp
            return pre

        def merge(l1, l2):
            print("l1 --> %s" % l1.val)
            print("l2 --> %s" % l2.val)
            dummy = ListNode(-1)
            nav = dummy
            while l1:
                nav.next = l1
                l1 = l1.next
                nav = nav.next
                print("nav --> %s" % nav.val)
                nav.next = l2
                if l2:
                    l2 = l2.next
                nav = nav.next
        mid = split(head)
        mid = reverse(mid)
        temp = mid
        while temp:
            print("%s, " % temp.val)
            temp = temp.next
        print("head --> ")
        temp = head
        while temp:
            print("%s, " % temp.val)
            temp = temp.next
        print()
        print("head --> %s" % head.val)
        print("mid --> %s" % mid.val)
        merge(head, mid)

