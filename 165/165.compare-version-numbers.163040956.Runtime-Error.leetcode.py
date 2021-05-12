class Solution(object):
    def compareVersion(self, version1, version2):
        arr1 = version1.split(".")
        arr2 = version2.split(".")
        i = 0

        while(i < len(arr1)):
            if int(arr2[i]) > int(arr1[i]):
                return -1

            if int(arr1[i]) > int(arr2[i]):
                return 1

            i += 1

        return 0

