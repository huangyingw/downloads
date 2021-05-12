import collections


class Solution(object):
    def isValidSudoku(self, board):
        dict_row, dict_col, dict_cell = collections.defaultdict(set), collections.defaultdict(set), collections.defaultdict(set)
        for row_index in range(1, 4):
            for col_index in range(1, 4):
                for row in range(3 * (row_index - 1), 3 * row_index):
                    for col in range(3 * (col_index - 1), 3 * col_index):
                        cell_data = board[row][col]
                        if cell_data == '.':
                            continue
                        if cell_data in dict_row[row] or cell_data in dict_col[col] or cell_data in dict_cell[(row_index, col_index)]:
                            return False
                        dict_row[row].add(cell_data)
                        dict_col[col].add(cell_data)
                        dict_cell[(row_index, col_index)].add(cell_data)
        return True

