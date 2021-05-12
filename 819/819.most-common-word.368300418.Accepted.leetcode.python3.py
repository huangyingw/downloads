from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph, banned):

        count = collections.Counter(piece for piece in re.split('[ !?\',;.]', paragraph.lower()) if piece)
        banned = set(banned)
        return max((item for item in count.items() if item[0] not in banned), key=operator.itemgetter(1))[0]

