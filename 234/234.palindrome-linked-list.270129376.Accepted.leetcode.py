class Solution:
    def isPalindrome(self, head):
        temp_list = []
        while head:
            temp_list.append(head.val)
            head = head.next
        l = len(temp_list)
        for i in range(0, l // 2):
            if temp_list[i] != temp_list[l - 1 - i]:
                return False
        return True

