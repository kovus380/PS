from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        answer = 0
        def dfs(i, j):
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == "0":
                return
            else:
                grid[i][j] = "0"

                dfs(i + 1, j)
                dfs(i, j + 1)
                dfs(i - 1, j)
                dfs(i, j - 1)

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1":
                    dfs(x, y)
                    answer += 1
        return answer
            


grid = [["1","0","1","1","0","1","1"]]
sol = Solution()
res = sol.numIslands(grid)
print(res)
