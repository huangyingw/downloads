class Solution(object):
    def solveNQueens(self, n):
        partials = [[]]
        for col in range(n):
            new_partials = []
            for partial in partials:
                for row in range(n):
                    if not self.conflict(partial, row):
                        new_partials.append(partial + [row])
            partials = new_partials
        results = []
        for partial in partials:
            result = [['.'] * n for _ in range(n)]
            for col, row in enumerate(partial):
                result[row][col] = 'Q'
            for row in range(n):
                result[row] = ''.join(result[row])
            results.append(result)
        return results

    def conflict(self, partial, new_row):
        for col, row in enumerate(partial):
            if new_row == row:
                return True
            col_diff = len(partial) - col
            if abs(new_row - row) == col_diff:
                return True
        return False

