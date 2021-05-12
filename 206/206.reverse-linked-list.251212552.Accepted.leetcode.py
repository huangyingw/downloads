class Solution(object):
    def reverseList(self, head):
        def dfs(head):
            if not head or not head.next:
                return head
            second = head.next
            ret = dfs(second)
            second.next = head
            print('ret --> %s' % (ret.val if ret else 'None'))
            return ret
        if not head:
            return head
        result = dfs(head)
        head.next = None
        return result

