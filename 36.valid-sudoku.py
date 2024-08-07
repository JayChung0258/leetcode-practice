#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#
from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        self.ROWS, self.COLS, = len(board), len(board[0])

        # 3 set to check
        # row_set = [set()] * 9  # wrong -> all set would be the same reference 
        # col_set = [set() for _ in range(9)] -> correct

        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        sub_set = defaultdict(set)

        for r in range(self.ROWS):
            for c in range(self.COLS):
                num = board[r][c]

                if num == ".":
                    continue

                if num in row_set[r] or num in col_set[c] or num in sub_set[(r//3,c//3)]:
                    return False
                
                row_set[r].add(num)
                col_set[c].add(num)
                sub_set[(r//3,c//3)].add(num)

        return True





# @lc code=end

