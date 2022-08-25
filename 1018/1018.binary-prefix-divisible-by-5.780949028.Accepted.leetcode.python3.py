class Solution(object):
    def prefixesDivBy5(self, A):
        result = []
        if not A:
            return []
        str_bin = ''
        for val in A:
            str_bin += str(val)
            if(int(str_bin, 2) % 5 == 0):
                result.append(True)
            else:
                result.append(False)
        return result

