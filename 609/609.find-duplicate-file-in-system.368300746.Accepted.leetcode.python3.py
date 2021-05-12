class Solution:

    def findDuplicate(self, paths):

        from collections import defaultdict
        d = defaultdict(list)
        for p in paths:
            path, *files = p.split()
            for file in files:
                content = file[file.index('(') + 1:-1]
                name = file[:file.index('(')]
                d[content].append('/'.join([path, name]))
        return list(v for v in d.values() if len(v) >= 2)

