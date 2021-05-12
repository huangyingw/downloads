class Solution(object):
    def reverseList(self, head):
        def dfs(head):
            if not head or not head.next:
                return head
            second = head.next
            dfs(second)
            second.next = head
            print('second --> %s' % (second.val if second else 'None'))
            return second
        if not head:
            return head
        result = dfs(head)
        head.next = None
        return result

