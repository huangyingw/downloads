class Solution(object):
    def reverseList(self, head):
        def dfs(head):
            if not head or not head.next:
                return head
            second = head.next
            ret = dfs(second)
            print('ret --> %s' % (ret.val if ret else 'None'))
            second.next = head
            print('second --> %s' % (second.val if second else 'None'))
            return second
        if not head:
            return head
        result = dfs(head)
        head.next = None
        return result

