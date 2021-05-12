class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words:
            return []
        word_len = len(words[0])
        print('word_len --> %s' % word_len)
        word_total = len(words) * word_len
        print('word_total --> %s' % word_total)
        ans = []
        word_cnt = collections.Counter(words)
        print('word_cnt --> %s' % word_cnt)
        rangeEnd = len(s) - word_total + 1
        print('rangeEnd --> %s' % rangeEnd)
        for i in range(min(word_len, rangeEnd)):
            start = i
            print('start --> %s' % start)
            cur_cnt = collections.Counter()
            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j: j + word_len]
                print('word --> %s' % word)
                if word in word_cnt:
                    cur_cnt[word] += 1
                    print('cur_cnt --> %s' % cur_cnt)
                    while cur_cnt[word] > word_cnt[word]:
                        cur_cnt[s[start: start + word_len]] -= 1
                        start += word_len
                else:
                    cur_cnt.clear()
                    start = j + word_len

                if(start + word_total == j):
                    print('start --> %s' % start)
                    ans.append(start)
        return ans

