class Solution(object):
    def wordPattern(self, pattern, str):
        words = str.split(' ')
        if len(words) != len(pattern):
            return False
        hashmap = {}
        for i in xrange(len(pattern)):
            if pattern[i] in hashmap:
                if hashmap[pattern[i]] != words[i]:
                    return False
            else:
                hashmap[pattern[i]] = words[i]
        return True

