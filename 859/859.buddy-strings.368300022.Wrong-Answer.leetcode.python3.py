class Solution:

    def buddyStrings(self, A, B):

        if set(A) != set(B):
            return False
        count = 0
        sum = 0
        for i, j in zip(A, B):
            if ord(i) - ord(j) != 0:
                sum += ord(i) - ord(j)
                count += 1
            if count > 2:
                return False

        return sum == 0 and count == 2 or (count == 0 and len(set(A)) < len(A))

