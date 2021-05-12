class Solution(object):
    def minArea(self, image, x, y):
        if not image:
            return 0

        top = self.searchTop(image, 0, x)
        bottom = self.searchBottom(image, x, len(image) - 1)
        left = self.searchLeft(image, 0, y)
        right = self.searchRight(image, y, len(image[0]) - 1)
        return (right - left + 1) * (bottom - top + 1)

    def searchTop(self, image, start, end):
        while start + 1 < end:
            mid = start + (end - start) / 2
            if ("1" in image[mid]) == True:
                end = mid
            else:
                start = mid
        if ("1" in image[start]) == True:
            return start
        elif ("1" in image[end]) == True:
            return end
        return end

    def searchBottom(self, image, start, end):
        while start + 1 < end:
            mid = start + (end - start) / 2
            if ("1" in image[mid]) == True:
                start = mid
            else:
                end = mid
        if ("1" in image[end]) == True:
            return end
        elif ("1" in image[start]) == True:
            return start
        return start

    def searchLeft(self, image, start, end):
        while start + 1 < end:
            mid = start + (end - start) / 2
            if any(image[k][mid] == "1" for k in range(len(image))) == True:
                end = mid
            else:
                start = mid
        if any(image[k][start] == "1" for k in range(len(image))) == True:
            return start
        elif any(image[k][start] == "1" for k in range(len(image))) == True:
            return end
        return end

    def searchRight(self, image, start, end):
        while start + 1 < end:
            mid = start + (end - start) / 2
            if any(image[k][mid] == "1" for k in range(len(image))) == True:
                start = mid
            else:
                end = mid
        if any(image[k][end] == "1" for k in range(len(image))) == True:
            return end
        elif any(image[k][start] == "1"for k in range(len(image))) == True:
            return start
        return start

