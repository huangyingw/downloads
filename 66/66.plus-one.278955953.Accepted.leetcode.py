class Solution(object):
    def plusOne(self, digits):
        AnsInt = 0
        Answer = []
        for digit in digits:
            AnsInt = int(digit) + 10 * AnsInt
        AnsInt += 1
        while AnsInt > 0:
            Append_Temp = AnsInt % 10
            Answer.append(Append_Temp)
            AnsInt = AnsInt / 10
        Answer.reverse()
        return Answer

