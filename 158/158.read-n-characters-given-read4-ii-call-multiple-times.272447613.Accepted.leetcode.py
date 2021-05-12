from collections import deque


class Solution(object):
    def __init__(self):
        self.leftover = deque()

    def read(self, buf, n):
        total_chars, added_chars, read_chars = 0, 4, 0
        while self.leftover and total_chars < n:
            buf[total_chars] = self.leftover.popleft()
            total_chars += 1
        while added_chars == 4 and total_chars < n:
            buf4 = [""] * 4
            read_chars = read4(buf4)
            added_chars = min(read_chars, n - total_chars)
            buf[total_chars:total_chars + added_chars] = buf4
            total_chars += added_chars
        while read_chars > added_chars:
            self.leftover.append(buf4[added_chars])
            added_chars += 1
        return total_chars

