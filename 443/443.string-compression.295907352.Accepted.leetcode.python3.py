class Solution:
    def compress(self, chars: List[str]) -> int:
        index = count = 0
        for i in range(len(chars)):
            count += 1
            if (i + 1 == len(chars)) or (chars[i] != chars[i + 1]):
                chars[index] = chars[i]
                index += 1
                if count > 1:
                    for j in str(count):
                        chars[index] = j
                        index += 1
                count = 0
        return index

