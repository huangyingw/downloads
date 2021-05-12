class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binary_numbers_list = []
        binary_numbers_list.append(head.val)
        while(head.next is not None):
            head = head.next
            binary_numbers_list.append(head.val)
        answer = 0
        power = 0

        for digit in range(len(binary_numbers_list) - 1, -1, -1):
            if(binary_numbers_list[digit] > 0):
                answer += ((2 ** power) * binary_numbers_list[digit])
            power += 1
        return answer

