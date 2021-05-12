class Solution:
    def toGoatLatin(self, S):
        words = S.split()
        vowels = set('aeiouAEIOU')
        ret = []
        for idx, word in enumerate(words, 1):
            if word[0] not in vowels:
                word = word[1:] + word[0]
            word += 'ma'
            word += 'a' * idx
            ret.append(word)
        return ' '.join(ret)

