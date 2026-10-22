class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # distance involved --> BFS
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        INF = 2147483647

        for r in range(ROWS):
            for c in range(COLS):
                # calculate shortest distance for inf cell 
                # start at 0 and get dist for each cell
                if grid[r][c] == 0:
                    q.append((r, c))
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # if cell not in bounds or cell is not inf --> skip the cell i.e., continue
                if nr not in range(ROWS) or nc not in range(COLS) or grid[nr][nc] != INF:
                    continue
                
                # cell is inf --> calculate dist --> update grid in place 
                grid[nr][nc] = grid[r][c] + 1
                q.append((nr, nc))
    
    # TC: O(m * n)
    # SC: O(m * n)