class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])

        if grid[0][0] == 1 or grid[r-1][c-1] == 1:
            return -1

        queue = deque()
        visited = set()
        queue.append((0,0))
        visited.add((0,0))
        length = 1
        while queue:
            for i in range(len(queue)):
                print (queue)
                sr, sc = queue.popleft()
                if sr == r - 1 and sc == c - 1:
                    return length
                cond  = [(0,1), (1,0), (-1,0), (0,-1), (1,-1), (-1,1), (-1,-1), (1,1)]
                for i, j in cond:
                    if (sr + i < 0 or sr + i == r or sc + j < 0 or sc + j == c or (sr + i, sc + j) in visited or grid[sr + i][sc + j] == 1):
                        continue;

                    queue.append((sr + i, sc + j))
                    visited.add((sr + i, sc + j))
            length += 1
        return -1