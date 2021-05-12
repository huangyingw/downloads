class Solution(object):
    def wordsTyping(self, sentences, rows, cols):
        sentence = '-'.join(sentences)
        sentence += '-'
        index_in_sentence = 0
        for row in range(rows):
            index_in_sentence += cols
            if sentence[(index_in_sentence % len(sentence))] == '-':
                index_in_sentence += 1
            else:
                while index_in_sentence > 0 and sentence[((index_in_sentence - 1) % len(sentence))] != '-':
                    index_in_sentence -= 1
        return index_in_sentence // len(sentence)

