class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()
        m, n = len(grid), len(grid[0])

        def check_neighbors(r, c):
            q = deque()
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            visited.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    r, c = row+dr, col+dc
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == '1' and (r,c) not in visited:
                        q.append((r,c))
                        visited.add((r,c))

        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1' and (r,c) not in visited:
                    islands += 1
                    check_neighbors(r,c)
        
        return islands