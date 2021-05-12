class Solution(object):
    def genKey(self, word):
        return ':'.join([
            str((ord(word[i]) - ord(word[i - 1])) % 26)
            for i in range(1, len(word))]
        )

    def groupStrings(self, strings):
        r = collections.defaultdict(list)

        for s in strings:
            r[self.genKey(s)].append(s)
        return [sorted(l) for l in r.values()]

