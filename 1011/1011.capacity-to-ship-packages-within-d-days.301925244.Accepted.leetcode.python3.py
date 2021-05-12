class Solution(object):
    def shipWithinDays(self, weights, D):
        high, low = sum(weights) + 1, max(weights)
        while(low < high):
            mid = (high + low) // 2
            temp_left = mid
            packet_at_left = D - 1
            for weight in weights:
                if weight <= mid:
                    if temp_left < weight:
                        if packet_at_left == 0:
                            low = mid + 1
                            break
                        packet_at_left -= 1
                        temp_left = mid - weight
                    else:
                        temp_left -= weight
            else:
                high = mid
        return low

