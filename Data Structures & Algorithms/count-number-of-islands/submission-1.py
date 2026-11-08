class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
            stack = []
            stack.append((r,c))
            visited.add((r,c))
            while stack:
                row, col = stack.pop()
                for dr, dc in directions:
                    if row + dr in range(rows) and col + dc in range(cols) and (row+dr, col+dc) not in visited and grid[row+dr][col+dc] == "1":
                        stack.append((row+dr,col+dc))
                        visited.add((row+dr,col+dc))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    res += 1
    
        return res