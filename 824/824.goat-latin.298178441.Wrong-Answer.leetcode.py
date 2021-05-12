class Solution:
    def toGoatLatin(self, S):
        if not S:
            return S
        aCount = 1
        vowelSet = set(list('aeiouAEIOU'))
        result = []
        for word in S.split():
            if word[0] not in vowelSet:
                word = word[1:] + word[0] + 'ma' + 'a' * aCount
            word = word + 'ma' + 'a' * aCount
            result.append(word)
            aCount += 1
        return ' '.join(result)

