class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = [0] * 26
        for note in magazine:
            a[ord(note) - ord('a')] += 1

        for note in ransomNote:
            index = ord(note) - ord('a')
            a[index] -= 1
            if a[index] < 0:
                return False

        return True

