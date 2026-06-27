class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        
        # if start and end cells are blocked -> return -1
        if grid[0][0] == 1 or grid[ROWS - 1][COLS - 1] == 1:
            return -1
        
        visited = set()

        directions = [[0, 1], [0, - 1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        
        q = deque()
        q.append([0, 0, 1])
        visited.add((0, 0))
        
        while q:
            row, col, length = q.popleft()

            # check if you have reached destination
            if row == ROWS - 1 and col == COLS - 1:
                return length

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                # check if cell in bounds and cell == 0 and cell not visited
                if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == 0 and (nr, nc) not in visited:                    
                    visited.add((nr, nc))
                    q.append([nr, nc, length + 1])
        
        return -1 
