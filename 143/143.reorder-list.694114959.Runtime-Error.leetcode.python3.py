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
                print("head --> %s" % head.val)
                nex = head.next
                if nex:
                    print("nex --> %s" % nex.val)
                head.next = pre
                pre = head
                head = nex
            if pre:
                print("pre --> %s" % pre.val)
            return pre

        def merge(l1, l2):
            print("l1 1 --> %s" % l1.val)
            print("l2 1 --> %s" % l2.val)
            dummy = ListNode(-1)
            nav = dummy
            while l1 or l2:
                nav.next = l1
                l1 = l1.next
                if l1:
                    print("l1 --> %s" % l1.val)
                nav = nav.next
                print("nav --> %s" % nav.val)
                nav.next = l2
                nav = nav.next
                if l2:
                    l2 = l2.next
                    print("l2 --> %s" % l2.val)
        mid = split(head)
        mid = reverse(mid)
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
        merge(head, mid)

