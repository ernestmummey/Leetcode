class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        num_islands = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    self.dfs(grid, r, c)
                    num_islands += 1
                    
        return num_islands
    
    def dfs(self,grid,r,c):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == '0':
            return
        
        grid[r][c] = '0'
            
        self.dfs(grid, r + 1, c)
        self.dfs(grid, r - 1, c)
        self.dfs(grid, r, c + 1)
        self.dfs(grid, r, c - 1)
                    