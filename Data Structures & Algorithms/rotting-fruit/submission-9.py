class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # BFS: Rot spreads from all rotten oranges at the same time, one step per minute.  
        # BFS spreads level by level the same way,

        # empty grid -> return -1
        if not grid:
            return -1 
        
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        # multi source bfs -> put all rotten oranges in q at the start
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                # keep track of fresh fruit to check at the end if no fresh fruit is left 
                if grid[r][c] == 1:
                    fresh += 1
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # to keep track of time for loop within while loop 
        time = 0

        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    # if cell not in bounds or cell is not fresh fruit do nothing
                    # if cell in bounds and cell is fresh fruit -> make it rotten -- add to q -- dec fresh
                    if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh -= 1
            time += 1

        # check if any fresh left
        if fresh == 0:
            return time
        else:
            return -1
                

    # TC: O(m * n)
    # SC: O(m * n)

