class Solution:

    def groupAnagrams(self, strs):

        ans = collections.defaultdict()
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()

    def groupAnagrams(strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()

