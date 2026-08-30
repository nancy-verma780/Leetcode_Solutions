class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # Track numbers present in rows, columns, and 3x3 boxes
        rows = [[False] * 9 for _ in range(9)]
        cols = [[False] * 9 for _ in range(9)]
        boxes = [[False] * 9 for _ in range(9)]

        # Initialize tracking arrays with existing numbers on the board
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    num = int(board[r][c]) - 1
                    box_idx = (r // 3) * 3 + (c // 3)
                    rows[r][num] = True
                    cols[c][num] = True
                    boxes[box_idx][num] = True

        def backtrack(r, c):
            # Move to the next row if we reach the end of the current column
            if c == 9:
                return backtrack(r + 1, 0)
            # If we finish all 9 rows, the puzzle is solved
            if r == 9:
                return True
            
            # Skip already filled cells
            if board[r][c] != '.':
                return backtrack(r, c + 1)

            box_idx = (r // 3) * 3 + (c // 3)

            # Try digits 1 through 9
            for num in range(9):
                if not rows[r][num] and not cols[c][num] and not boxes[box_idx][num]:
                    # Place the digit
                    board[r][c] = str(num + 1)
                    rows[r][num] = cols[c][num] = boxes[box_idx][num] = True

                    # Recurse to the next cell
                    if backtrack(r, c + 1):
                        return True

                    # Backtrack (undo the choice)
                    board[r][c] = '.'
                    rows[r][num] = cols[c][num] = boxes[box_idx][num] = False

            return False

        backtrack(0, 0)
