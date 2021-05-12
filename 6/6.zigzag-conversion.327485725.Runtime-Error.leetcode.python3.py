class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for strr in strs:
            ans[''.join(sorted(strr))].append(strr)

        return ans.values()


class Solution0:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for strr in strs:
            sort_strr = ''.join(sorted(strr))
            if sort_strr not in ans.keys():
                ans[sort_strr] = []
            ans[sort_strr].append(strr)

        return ans.values()


class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for strr in strs:

            KEY = [0] * 26
            for letter in strr:
                KEY[ord(letter) - ord('a')] += 1
            ans[tuple(KEY)].append(strr)

        return ans.values()

