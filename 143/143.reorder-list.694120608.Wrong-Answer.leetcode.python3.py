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
                l2 = l2.next
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
        merge(head, mid)

