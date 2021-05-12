class Solution:
    def read(self, buf, n):
        total_chars, last_chars, buf4 = 0, 4, [""] * 4
        while last_chars == 4 and total_chars < n:
            last_chars = min(read4(buf4), n - total_chars)
            buf[total_chars:total_chars + last_chars] = buf4
            total_chars += last_chars
        return total_chars

