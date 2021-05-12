class Solution(object):
    def maxEnvelopes(self, envelopes):
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        nested = []

        def bin_search(target):
            left, right = 0, len(nested)
            while left < right:
                mid = (left + right) // 2
                if target > nested[mid]:
                    left = mid + 1
                elif target == nested[mid]:
                    return mid
                else:
                    right = mid - 1
            return left
        for _, h in envelopes:
            i = bin_search(h)
            if i == len(nested):
                nested.append(h)
            else:
                nested[i] = h
        return len(nested)

