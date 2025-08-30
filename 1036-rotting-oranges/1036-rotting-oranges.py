class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        
        # Step 1: Add all rotten oranges to queue, count fresh
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c, 0))  # (row, col, time)
                elif grid[r][c] == 1:
                    fresh += 1
        
        # If no fresh oranges at all
        if fresh == 0:
            return 0
        
        # Step 2: BFS
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        time = 0
        
        while q:
            r, c, t = q.popleft()
            time = max(time, t)
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2  # rot it
                    fresh -= 1
                    q.append((nr, nc, t+1))
        
        # Step 3: Check if fresh oranges remain
        return time if fresh == 0 else -1
