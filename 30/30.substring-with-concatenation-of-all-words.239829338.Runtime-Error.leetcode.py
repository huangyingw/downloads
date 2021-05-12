class Solution(object):
    def findSubstring(self, s, words):
        ls = len(s)
        word_ls = len(words[0])
        target_dict = {}
        # create a targe dict for match
        for word in words:
            try:
                target_dict[word] += 1
            except KeyError:
                target_dict[word] = 1
        res = []
        for start in range(ls - word_ls * len(words) + 1):
            curr_dict = target_dict.copy()
            for pos in range(start, start + word_ls * len(words), word_ls):
                curr = s[pos:pos + word_ls]
                try:
                    curr_dict[curr] -= 1
                    # word appears more than target
                    if curr_dict[curr] < 0:
                        break
                except KeyError:
                    # word not in words
                    break
            else:
                # all word in target dict
                res.append(start)
        return res

