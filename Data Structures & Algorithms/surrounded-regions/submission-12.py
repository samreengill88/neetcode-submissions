class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(r, c):
            
            # stop if cell not in bounds or if cell is not O 
            if r not in range(ROWS) or c not in range(COLS) or board[r][c] != 'O':
                return 
            
            board[r][c] = 'T'
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)
            

        ######## find border cells with O ##############
        # traverse rows for borders
        for r in range(ROWS):
            # left col
            if board[r][0] == 'O':
                dfs(r, 0)
            # right col
            if board[r][COLS - 1] == 'O':
                dfs(r, COLS - 1)
        for c in range(COLS):
            # top row
            if board[0][c] == 'O':
                dfs(0, c)
            # bottom row
            if board[ROWS - 1][c] == 'O':
                dfs(ROWS - 1, c)

        # traverse cols 
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'T':
                    board[r][c] = 'O'












