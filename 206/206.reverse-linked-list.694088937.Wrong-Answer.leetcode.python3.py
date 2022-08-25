class Solution(object):
    def reverseList(self, head):
        def dfs(head):
            if not head or not head.next:
                print("head --> %s" % head.val)
                return head
            second = head.next
            ret = dfs(second)
            second.next = head
            print("second --> %s" % second.val)
            return second
        if not head:
            return head
        result = dfs(head)
        print("result --> %s" % result.val)
        head.next = None
        return result

