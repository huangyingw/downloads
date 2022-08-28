class Solution(object):
    def maxScore(self, cardPoints, k):
        left = 0
        right = len(cardPoints) - k
        print("cardPoints --> %s" % cardPoints[len(cardPoints) - k:])
        ksum = sum(cardPoints[len(cardPoints) - k:])
        print("ksum --> %s" % ksum)
        result = max(float('-inf'), ksum)
        while right < len(cardPoints):
            ksum = ksum - cardPoints[right] + cardPoints[left]
            print("ksum --> %s" % ksum)
            result = max(result, ksum)
            left += 1
            right += 1
        return result

