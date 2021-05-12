class Solution(object):
    def judgeCircle(self, moves):
        walk = {'U': 1, 'L': 1, 'D': -1, 'R': -1}
        stepLR, stepUD = 0, 0
        for move in moves:
            if move in ['L', 'R']:
                stepLR += walk[move]
            else:
                stepUD += walk[move]
        return (stepUD == 0) & (stepLR == 0)

