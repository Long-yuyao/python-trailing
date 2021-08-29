"""
input:grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
output:3
"""


# bfs
# dfs
class Solution:
    def __init__(self):
        self.ans = 0
        self.grid = None
        self.m = None
        self.n = None

    def numIslands(self, grid: list) -> int:
        if not grid:
            return self.ans
        self.m = len(grid)
        self.n = len(grid[0])
        self.grid = grid
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == '1':
                    self.bfs(i, j)
                    self.ans = self.ans + 1
        return self.ans

    def bfs(self, i, j):
        if 0 <= i < self.m and 0 <= j < self.n:
            if self.grid[i][j] == '1':
                self.grid[i][j] = '0'
                self.bfs(i + 1, j)
                self.bfs(i - 1, j)
                self.bfs(i, j-1)
                self.bfs(i, j+1)


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
ans = Solution()
assert ans.numIslands(grid) == 3
