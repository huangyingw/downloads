class Solution(object):
    def numberOfPatterns(self, m, n):
        skips = [(1, 7, 4), (1, 9, 5), (1, 3, 2), (2, 8, 5),
                 (3, 7, 5), (3, 9, 6), (4, 6, 5), (7, 9, 8)]
        jumps = {}
        for start, end, skip in skips:
            jumps[(start, end)] = skip
            jumps[(end, start)] = skip

        def count_patterns(start):
            paths = [[{start}, start]]
            patterns = 1 if m == 1 else 0
            for length in range(2, n + 1):
                new_paths = []
                for visited, last in paths:
                    for extension in range(1, 10):
                        if extension in visited:
                            continue
                        if (last, extension) in jumps and jumps[(last, extension)] not in visited:
                            continue
                        new_visited = set(visited)
                        new_visited.add(extension)
                        new_paths.append([new_visited, extension])
                paths = new_paths
                if length >= m:
                    patterns += len(paths)
            return patterns
        return 4 * count_patterns(1) + 4 * count_patterns(2) + count_patterns(5)

