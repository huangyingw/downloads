class Solution(object):
    def reverseList(self, head):
        def dfs(head):
            if not head or not head.next:
                return head
            second = head.next
            ret = dfs(second)
            second.next = head
            print("second --> %s" % second.val)
            return ret
        result = dfs(head)
        if head:
            head.next = None
        print("result --> %s" % result.val)
        return result

