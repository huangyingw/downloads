class Solution(object):
    def findSubstring(self, s, words):
        if not str or not words:
            return []

        counts = {}
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1

        result = []
        n, numOfWords, fixLen = len(s), len(words), len(words[0])

        for index in range(0, n - numOfWords * fixLen + 1):
            seen = {}

            index_j = 0
            while index_j < numOfWords:
                word = s[index + index_j * fixLen: index + (index_j + 1) * fixLen]
                if word in counts:
                    if word in seen:
                        seen[word] += 1
                    else:
                        seen[word] = 1

                    if seen[word] > counts[word]:
                        break
                else:
                    break
                index_j += 1

            if index_j == numOfWords:
                result.append(index)

        return

