class Solution:
    def uniqueMorseRepresentations(self, words):

        concatenation = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        letter = "abcdefghijklmnopqrstuvwxyz"
        mapping = dict(zip(letter, concatenation))
        return len(set("".join([mapping[c] for c in word]) for word in words))

