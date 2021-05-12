class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        cur_max = max_vowels = 0

        for i in range(len(s)):
            if s[i] in vowels:
                cur_max += 1

            if i >= k and s[i - k] in vowels:
                cur_max -= 1

            max_vowels = max(max_vowels, cur_max)

        return max_vowels

