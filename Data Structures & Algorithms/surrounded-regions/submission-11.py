class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # dfs 
        # 
        ROWS, COLS = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        ## step 3 ##
        def dfs(r, c):
            # base case: if cell not in bounds or cell not 0  -> return do nothing
            if r not in range(ROWS) or c not in range(COLS) or board[r][c] != 'O':
                return 
            
             # Mark an O and every O connected to it as safe ('T')
            board[r][c] = 'T'

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)




        ######## step 1. find border cells with O ##############
        # start DFS from every O on the border.
        # scan rows 
        for r in range(ROWS):
            if board[r][0] == 'O':
                dfs(r, 0)
            if board[r][COLS - 1] == 'O':
                dfs(r, COLS - 1)
        # scan cols 
        for c in range(COLS):
            if board[0][c] == 'O':
                dfs(0, c)
            if board[ROWS - 1][c]:
                dfs(ROWS - 1, c)
        ##############################################

        # step 2

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O": # trapped O's ->. turn them to X
                     board[r][c] = 'X'
                elif board[r][c] == "T": # safe, were marked as T -- flip them back to O
                     board[r][c] = 'O'

        