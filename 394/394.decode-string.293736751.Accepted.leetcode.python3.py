class Solution(object):
    def decodeString(self, s):
        self.i = 0
        return "".join(self.decode(s))

    def decode(self, s):
        result = []
        while self.i < len(s) and s[self.i] != "]":
            if s[self.i] not in "0123456789":
                result.append(s[self.i])
                self.i += 1
            else:
                repeats = 0
                while s[self.i] in "0123456789":
                    repeats = repeats * 10 + int(s[self.i])
                    self.i += 1
                self.i += 1
                result += (self.decode(s) * repeats)
                self.i += 1
        return result

