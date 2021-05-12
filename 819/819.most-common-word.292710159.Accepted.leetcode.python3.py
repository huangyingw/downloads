class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        banned = set(banned)
        count = collections.Counter(word for word in re.split('[ !?\',;.]', paragraph.lower()) if word)
        return max((item for item in count.items() if item[0] not in banned), key=operator.itemgetter(1))[0]

