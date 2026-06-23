class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        INF = 2147483647

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0: # run bfs on gate when cell is 0 -> so add it to queue
                    q.append((r, c))
        
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
        # while q is not empty
        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # if cell not in bounds or cell is not inf then continue
                if( 
                    not(nr in range(rows)) or
                    not(nc in range(cols)) or
                    grid[nr][nc] != INF
                ):
                    continue
                
                # we know cell is inf, calculate dist
                grid[nr][nc] = grid[r][c] + 1
                q.append((nr, nc))

