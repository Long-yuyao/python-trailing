# https://leetcode-cn.com/problems/01-matrix/


class Solution:
    def updateMatrix(self, mat: list) -> list:
        stack = []
        visited = [[0] * len(mat[0]) for _ in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    visited[i][j] = 1
                    stack.append([i, j])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        step = 0
        while stack:
            count = len(stack)
            for i in range(count):
                if mat[stack[0][0]][stack[0][1]] != 0:
                    mat[stack[0][0]][stack[0][1]] = step
                for dx, dy in dirs:
                    x = stack[0][0] + dx
                    y = stack[0][1] + dy
                    if 0 <= x < len(mat) and 0 <= y < len(mat[0]) and visited[x][y] == 0:
                        stack.append([x, y])
                        visited[x][y] = 1
                stack.pop(0)
            step = step + 1
        return mat


print(Solution().updateMatrix([[0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0]]))
