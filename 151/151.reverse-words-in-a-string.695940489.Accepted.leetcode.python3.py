class Solution(object):
    def reverseWords(self, s):
        if not s:
            return ""
        arr = s.split(" ")
        sb = ""
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] != "":
                sb += arr[i]
                sb += " "
        return "" if not sb else sb[: -1]

