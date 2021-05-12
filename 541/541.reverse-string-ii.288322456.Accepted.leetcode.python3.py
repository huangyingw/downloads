class Solution:
    def reverseStr(self, s, k):
        s = list(s[0 + i:k + i] for i in range(0, len(s), k))
        output = []
        for j in range(len(s)):
            if j % 2 == 0:
                output.append(s[j][::-1])
            else:
                output.append(s[j])
        return "".join(output)

