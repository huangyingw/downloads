class Solution:
    def toLowerCase(self, str):
        result = ""
        for c in str:
            if c >= "A" and c <= "Z":
                result = result + chr(ord(c) + ' ')
            else:
                result = result + c
        return result

