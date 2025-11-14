class Solution:
  def solveNQueens(self, n: int) -> list[list[str]]:
    result = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    occupied_cols = set()
    occupied_pos_diagonals = set()
    occupied_neg_diagonals = set()

    def backtrack(row):
      if row == n:
        result.append(["".join(r) for r in board])
        return

      for col in range(n):
        pos_diagonal_id = row + col
        neg_diagonal_id = row - col

        if (col in occupied_cols or
            pos_diagonal_id in occupied_pos_diagonals or
            neg_diagonal_id in occupied_neg_diagonals):
          continue

        board[row][col] = 'Q'
        occupied_cols.add(col)
        occupied_pos_diagonals.add(pos_diagonal_id)
        occupied_neg_diagonals.add(neg_diagonal_id)

        backtrack(row + 1)

        board[row][col] = '.'
        occupied_cols.remove(col)
        occupied_pos_diagonals.remove(pos_diagonal_id)
        occupied_neg_diagonals.remove(neg_diagonal_id)

    backtrack(0)
    return result