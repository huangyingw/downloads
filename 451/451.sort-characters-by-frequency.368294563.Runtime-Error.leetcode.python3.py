"""
Given a string, sort it in decreasing order based on the frequency of characters.
Example 1:
Input:
"tree"
Output:
"eert"
Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:
Input:
"cccaaa"
Output:
"cccaaa"
Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:
Input:
"Aabb"
Output:
"bbAa"
Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""
from collections import Counter


class Solution:

    def frequencySort1(self, s):
        mapping = sorted(((idx, v) for idx, v in Counter(s).items()), key=lambda item: item[1], reverse=True)
        return "".join([idx * v for (idx, v) in mapping])

    def frequencySort2(self, s):
        c = Counter(s).most_common(len(s))
        return ''.join([i[1] * i[0] for i in c])

