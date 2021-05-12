class Solution(object):
    def wordPatternMatch(self, pattern, str):
        m, n = len(pattern), len(str)

        def is_match(i, j):
            if i == m and j == n:
                return True
            if i == m or j == n:
                return False
            for end in range(j, n - (m - i) + 1):
                p, test_s = pattern[i], str[j:end + 1]
                if p not in mapping and test_s not in s_used:
                    mapping[p] = test_s
                    s_used.add(test_s)
                    if is_match(i + 1, end + 1):
                        return True
                    del mapping[p]
                    s_used.discard(test_s)
                elif p in mapping and mapping[p] == test_s:
                    if is_match(i + 1, end + 1):
                        return True
            return False
        mapping = {}
        s_used = set()
        return is_match(0, 0)

