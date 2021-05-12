class Solution(object):
    def reverseWords(self, str):
        def reverse(str, begin, end):
            while begin < end:
                temp = str[begin]
                str[begin] = str[end]
                str[end] = temp
                begin += 1
                end -= 1
        reverse(str, 0, len(str) - 1)
        begin, end = 0, 0

        while end <= len(str):
            if end == len(str) or str[end] == ' ':
                reverse(str, begin, end - 1)

                while end < len(str) and str[end] == ' ':
                    end += 1
                begin = end
            end += 1

