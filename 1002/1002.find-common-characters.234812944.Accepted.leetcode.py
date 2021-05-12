class Solution(object):
    def commonChars(self, A):
        char_map = {}
        for char in A[0]:
            if char in char_map:
                char_map[char] += 1
            else:
                char_map[char] = 1
        for word in A[1:]:
            for char in char_map.keys():
                if char in word:
                    char_count = min(word.count(char), char_map[char])
                    char_map[char] = char_count
                else:
                    del char_map[char]
        result = []
        for key, value in char_map.items():
            result += [key] * value
        return result

