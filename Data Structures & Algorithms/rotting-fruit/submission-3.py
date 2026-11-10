class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        mins, fresh = 0, 0
        q = collections.deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        mins = 0
        while q and fresh > 0:
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr in range(len(grid)) 
                    and nc in range(len(grid[0])) 
                    and grid[nr][nc] == 1):
                        q.append((nr, nc))
                        grid[nr][nc] = 3
                        fresh -= 1
            mins += 1
        return mins if fresh == 0 else -1

                