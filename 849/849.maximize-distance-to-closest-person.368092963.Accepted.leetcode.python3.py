class Solution:

    def maxDistToClosest(self, seats):

        max_dis = 0
        cur_dis = 0
        for value in seats:
            if value == 0:
                cur_dis += 1
            else:
                max_dis = max(max_dis, cur_dis)
                cur_dis = 0
        head_dis = seats.index(1)
        tail_dis = cur_dis
        max_dis = ((max_dis + 1) // 2, head_dis, tail_dist)
        return max_dis

    def maxDistToClosest(self, seats):
        start, end = 0, len(seats) - 1
        while seats[start] == 0:
            start += 1
        while seats[end] == 0:
            end -= 1
        max_dist, dist = 0, 0
        for i in range(start, end + 1):
            if seats[i] == 1:
                if dist > max_dist:
                    max_dist = dist
                dist = 0
            else:
                dist += 1
        return max(math.ceil(max_dist / 2), start, len(seats) - end - 1)

