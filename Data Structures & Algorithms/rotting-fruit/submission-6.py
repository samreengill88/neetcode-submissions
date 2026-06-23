class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # empty grid
        if not grid:
            return -1
        
        # count fresh fruit - if any fresh left at the end return -1 else return time
        # if rotten fruit - run BFS
        ROWS = len(grid)
        COLS = len(grid[0])
        fresh = 0
        time = 0

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = deque()



        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                
                # rotten
                if grid[r][c] == 2:
                    q.append((r, c))
      
        while q and fresh > 0:
            

            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # if cell in bounds and cell is fresh
                    if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == 1:
                        # make it rotten, add to q , dec fresh
                        grid[nr][nc]  = 2
                        q.append((nr, nc))
                        fresh -= 1
            time += 1



        
        if fresh > 0:
            return -1 
        else:
            return time 

        