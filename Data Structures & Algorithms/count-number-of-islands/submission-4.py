class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def dfs(r, c):
            if r > rows - 1 or r < 0 or c > cols - 1 or c < 0:
                return
            if grid[r][c] == "1" and not tuple([r, c]) in visited:
                visited.add(tuple([r,c]))
            else:
                return
            for dr, dc in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if tuple([r, c]) in visited or grid[r][c] == "0":
                    continue
                else:
                    islands += 1
                    dfs(r, c)
        return islands