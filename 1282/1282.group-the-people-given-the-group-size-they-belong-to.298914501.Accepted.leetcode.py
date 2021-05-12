class Solution(object):
    def groupThePeople(self, groupSizes):

        count = collections.defaultdict(list)
        for i, size in enumerate(groupSizes):
            count[size].append(i)
        result = []
        for s, value in count.items():
            for index in range(0, len(value), s):
                result.append(value[index:index + s])
        return result

