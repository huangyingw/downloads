class Solution(object):
    def compareVersion(self, version1, version2):
        v1Arr = version1.split(".")
        v2Arr = version2.split(".")
        len1 = len(v1Arr)
        len2 = len(v2Arr)
        lenMax = max(len1, len2)

        for x in range(lenMax):
            v1Token = int(v1Arr[x])if x < len1 else 0
            v2Token = int(v2Arr[x])if x < len2 else 0

            if v1Token < v2Token:
                return -1

            if v1Token > v2Token:
                return 1
        return 0

