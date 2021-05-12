class Solution(object):
    def wordPatternMatch(self, pattern, str):
        d, used = {}, {}
        return self.match(pattern, str, d, used)

    def match(self, pattern, str, d, used):
        if len(pattern) == 0 and len(str) == 0:
            return True
        elif len(pattern) == 0 or len(str) == 0:
            return False

        if len(pattern) == 1:
            if pattern in d:
                if d[pattern] == str:
                    return True
                else:
                    return False
            else:
                if str in used and used[str]:
                    return False
                else:
                    return True

        if pattern[0] in d:
            if str.find(d[pattern[0]]) != 0:
                return False
            else:
                result = self.match(pattern[1:], str[len(d[pattern[0]]):], d, used)
                if result:
                    return True
        else:
            length = len(str) - (len(pattern) - 1)
            for i in range(length):
                cur = str[:i + 1]
                if cur in used and used[cur]:
                    continue
                used[cur] = True
                d[pattern[0]] = cur
                result = self.match(pattern[1:], str[len(cur):], d, used)
                del d[pattern[0]]
                if result:
                    return True
                del used[cur]

        return False

