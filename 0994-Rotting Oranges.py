class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_count = 0
        rotten = deque()
        num_rows, num_cols = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        max_time = 0

        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == 1:
                    fresh_count += 1
                elif grid[r][c] == 2:
                    rotten.append((r, c, 0))
        
        while rotten:
            row, col, time = rotten.popleft()
            max_time = max(max_time, time)

            for dr, dc in directions:
                r, c = row+dr, col+dc
                if 0 <= r < num_rows and 0 <= c < num_cols and grid[r][c] == 1:
                    grid[r][c] = 2
                    rotten.append((r, c, time+1))
                    fresh_count -= 1
        
        return max_time if fresh_count == 0 else -1