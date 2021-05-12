class Solution(object):
    def generatePalindromes(self, s):
        ret = []
        if True:
            chars = dict()
            for letter in s:
                if letter not in chars:
                    chars[letter] = 1
                else:
                    chars[letter] += 1
            halfChars = []
            mid = ''
            singletonCount = 0
            for char, count in chars.iteritems():
                if count % 2 == 1:
                    mid = char
                    singletonCount += 1
                    if singletonCount > 1:
                        return ret
                halfChars += [char] * (count / 2)

            ret = self.permute(list(halfChars))
            ret = map(lambda x: "".join(x + [mid] + x[::-1]), ret)

        return ret

    def permute(self, letters):
        ret = []
        used = [False] * len(letters)
        letters.sort()
        self.dfs(letters, [], used, ret)
        return ret

    def dfs(self, letters, path, used, ret):
        if len(path) == len(letters):
            ret.append(path[:])
            return

        for i in xrange(len(letters)):
            if used[i] == True:
                continue
            if i > 0 and letters[i] == letters[i - 1] and used[i - 1] == False:
                continue
            path.append(letters[i])
            used[i] = True
            self.dfs(letters, path, used, ret)
            path.pop()
            used[i] = False

