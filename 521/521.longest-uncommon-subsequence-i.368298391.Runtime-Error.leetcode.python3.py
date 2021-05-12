When len(A) == len(B), the only subsequence of B equal to A is B
so as long as A != B, the answer remains len(A).
When A == B, any subsequence of A can be found in B and vice versa, so the answer is -1.


class Solution:
    def findLUSlength(self, a, b):

        if a == b:
            return -1
        return max(len(a), len(b))

