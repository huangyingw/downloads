class Solution(object):
    def reverseWords(self, s):
        if not s:
            return ""

        arr = s.split(" ")
        sb = []

        for i in range(len(arr) - 1, -1, -1):
            if arr[i] != "":
                sb.append(arr[i]).append(" ")

        return "" if not sb else sb[0, len(sb) - 1]

