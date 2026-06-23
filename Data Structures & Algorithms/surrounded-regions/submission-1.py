class Solution:
    def solve(self, board: List[List[str]]) -> None:

        # 1. change all border 0 -> T
        # 2. Change Remaining 0 -> X
        # 3. change T -> 0

        ROWS = len(board)
        COLS = len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        
        def bfs():
            q = deque()
            for r in range(ROWS):
                for c in range(COLS):
                    if (r == 0 or r == ROWS - 1 or c == 0 or c == COLS -1) and board[r][c]:
                        q.append((r, c)) # all border cells -> added to q
                        
                    
            while q:
                r, c = q.popleft()
                if board[r][c] == "O":
                    board[r][c] = "T"
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if nr in range(ROWS) and nc in range(COLS):
                            # if board[nr][nc] == 'O':
                            #     board[nr][nc] = 'X'
                            q.append((nr, nc))


        bfs()
        
        # 2 and 3
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'T':
                    board[r][c] = 'O'
        