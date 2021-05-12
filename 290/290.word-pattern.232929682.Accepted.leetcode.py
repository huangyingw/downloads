class Solution(object):
    def wordPattern(self, pattern, str):
        words = str.split(' ')
        if len(words) != len(pattern):
            return False
        hashmap = {}
        mapval = {}
        for i in xrange(len(pattern)):
            if pattern[i] in hashmap:
                if hashmap[pattern[i]] != words[i]:
                    return False
            else:
                if words[i] in mapval:
                    return False
                hashmap[pattern[i]] = words[i]
                mapval[words[i]] = True
        return True

