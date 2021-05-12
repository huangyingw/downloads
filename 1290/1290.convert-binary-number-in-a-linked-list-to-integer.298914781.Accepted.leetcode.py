class Solution(object):
    def getDecimalValue(self, head):

        result = ''
        if not head:
            return 0
        while head:
            result += str(head.val)
            head = head.next
        return int(result, 2)

