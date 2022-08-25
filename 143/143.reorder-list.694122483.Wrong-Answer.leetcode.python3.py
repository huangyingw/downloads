class Solution(object):
    def reorderList(self, head):
        def split(head):
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            result = slow.next
            slow.next = None
            print("result --> %s" % result.val)
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
            print("l1 1 --> %s" % l1.val)
            print("l2 1 --> %s" % l2.val)
            dummy = ListNode(-1)
            nav = dummy
            while l2:
                nav.next = l1
                nav = nav.next
                print("nav --> %s" % nav.val)
                nav.next = l2
                nav = nav.next
                print("nav --> %s" % nav.val)
                l1 = l1.next
                print("l1 --> %s" % l1.val)
                l2 = l2.next
                if l2:
                    print("l2 --> %s" % l2.val)
        mid = split(head)
        mid = reverse(mid)
        print("mid --> %s" % mid.val)
        print("mid --> ")
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

