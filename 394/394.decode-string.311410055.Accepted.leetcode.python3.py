class Solution(object):
    def decodeString(self, s):
        stack = []
        repeats = 0
        for c in s:
            if c == "]":
                item = stack.pop()
                current = []
                while not isinstance(item, int):
                    current.append(item)
                    item = stack.pop()
                stack += (current[::-1] * item)
            elif c.isnumeric():
                repeats = repeats * 10 + int(c)
            elif c == "[":
                stack.append(repeats)
                repeats = 0
            else:
                stack.append(c)
        return "".join(stack)

