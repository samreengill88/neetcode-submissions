class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # empty grid - return -1
        # use BFS
        # keep track of fresh oranges, if not 0 at the end return -1 else return time 
        # run bfs on fresh oranges 

        q = collections.deque()
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        time = 0

        if not grid:
            return -1

        for r in range(rows):
            for c in range(cols):
                # track if its an orange 
                if grid[r][c] == 1:
                    fresh += 1
                # orange is rotten - run bfs, so add it to queue
                if grid[r][c] == 2:
                    q.append((r, c))
             
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        # stop when q is empty and fresh = 0 
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    # if in bounds and orange is fresh, make them rotten
                    # if not this do nothing, continue
                    nr, nc = r + dr, c + dc

                    if (not(nr in range(rows)) or
                        not(nc in range(cols)) or
                        (grid[nr][nc] != 1)):
                        continue
                
                    # make it rotten
                    grid[nr][nc] = 2
                    q.append((nr, nc))
                    fresh -= 1 
            time += 1

        # if fresh is not 0 return -1, otherwise return time
        if fresh != 0:
            return -1
        return time

        