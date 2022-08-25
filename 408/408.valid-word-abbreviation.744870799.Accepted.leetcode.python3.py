class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        i, j = 0, 0
        while j < len(abbr):
            if abbr[j] == "0":
                return False
            if abbr[j] < "a":
                count = 0
                while j < len(abbr) and abbr[j] < "a":
                    count = count * 10 + int(abbr[j])
                    j += 1
                i += count
            else:
                if i >= len(word) or abbr[j] != word[i]:
                    return False
                i += 1
                j += 1
        return i == len(word)

