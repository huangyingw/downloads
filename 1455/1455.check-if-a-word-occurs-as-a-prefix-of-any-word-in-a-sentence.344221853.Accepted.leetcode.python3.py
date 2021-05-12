class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = ' ' + sentence
        searchWord = ' ' + searchWord
        word = j = 0
        for i in range(len(sentence)):
            word += sentence[i] == ' '

            j = j + 1 if sentence[i] == searchWord[j] else 0

            if j == len(searchWord):
                return word

        return -1

