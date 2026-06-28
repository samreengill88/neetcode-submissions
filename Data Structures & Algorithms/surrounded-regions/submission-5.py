class Solution:
    def solve(self, board: List[List[str]]) -> None:


        ROWS, COLS = len(board), len(board[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(r, c):

            # if cell is out of bounds or if its not O -> do nothing return 
            if not(r in range(ROWS)) or not(c in range(COLS)) or board[r][c] != 'O':
                return 
            
            # know valid cell and cell == 'O' -> change to T
            board[r][c] = 'T'

            # call dfs on all its neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)



        # start dfs from border O's
        for r in range(ROWS):
            if board[r][0] == 'O': # right border
                dfs(r, 0)
            if board[r][COLS - 1] == 'O': # left border
                dfs(r, COLS - 1)

        for c in range(COLS):
            if board[0][c] == 'O':
                dfs(0, c)
            if board[ROWS - 1][c]:
                dfs(ROWS - 1, c)


        # starting from boarder -> change all safe O's to T (not surrounded)
        # Do not touch remaining O's (need to be flipped to 'X')
        # Then change T -> O
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'T':
                    board[r][c] = 'O'