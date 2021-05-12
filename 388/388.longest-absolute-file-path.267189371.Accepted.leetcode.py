class Solution(object):
    def lengthLongestPath(self, input):
        if input is None or len(input) == 0:
            return 0
        lines = input.split('\n')
        last_level_len = [0] * (len(lines) + 1)
        max_len = 0
        for line in lines:
            try:
                level = line.rindex('\t') + 1
            except:
                level = 0
            cur_len = last_level_len[level + 1] = last_level_len[level] + len(line) - level + 1
            if '.' in line:
                max_len = max(max_len, cur_len - 1)
        return max_len

