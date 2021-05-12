class Solution:
    def checkRecord(self, s):
        return False if bool(re.search(r"(L){3,}", s)) or bool(re.search(r"(A).*\1", s)) else True

