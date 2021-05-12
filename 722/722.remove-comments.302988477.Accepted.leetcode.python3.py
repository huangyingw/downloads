class Solution(object):
    def removeComments(self, source):
        removed = []
        comment_block = False
        new_line = []
        for line in source:
            i = 0
            while i < len(line):
                test = line[i:i + 2]
                if not comment_block and test == "/*":
                    comment_block = True
                    i += 2
                elif not comment_block and test == "//":
                    i = len(line)
                elif comment_block and test == "*/":
                    comment_block = False
                    i += 2
                elif comment_block:
                    i += 1
                else:
                    new_line.append(line[i])
                    i += 1
            if not comment_block and new_line:
                removed.append("".join(new_line))
                new_line = []
        if new_line:
            removed.append("".join(new_line))
        return removed

