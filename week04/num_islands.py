import collections


class Solution:
    @staticmethod
    def num_islands1(grid):
        """
        广度优先
        遍历二维数组中的每个元素
        如果当前元素为1，即陆地。计数加一。
        创建队列并加入队列中，并将当前节点置为0，代表已访问过。
        while循环创建的队列。
        对当前节点四个方向进行搜索，如果当前节点是1，加入队列中。注意判断边界。
        对访问过的节点置为0 ，代表已访问。
        :param grid:
        :return:
        """
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    count += 1
                    grid[row][col] = '0'

                    land_positions = collections.deque()
                    land_positions.append([row, col])
                    while len(land_positions) > 0:
                        r, c = land_positions.popleft()
                        for r_, c_ in [[r, c + 1], [r, c - 1], [r + 1, c], [r - 1, c]]:
                            if 0 <= r_ < len(grid) and 0 <= c_ < len(grid[0]) and grid[r_][c_] == '1':
                                grid[r_][c_] = '0'
                                land_positions.append([r_, c_])
        return count

    @staticmethod
    def num_islands2(grid):
        """
        深度优先。
        便利二维数组中的每一个元素。
        如果元素等于1。对该元素的四个方向进行递归。
        当元素等于1时，递归终止。
        递归中访问过的元素置为0，代表已访问过。
        :param grid:
        :return:
        """
        if not grid:
            return 0

        def dfs(grid_, row, col):
            if row < 0 or col < 0 or row >= len(grid_) or col >= len(grid_[0]) or grid_[row][col] != '1':
                return
            grid_[row][col] = '0'
            dfs(grid_, row + 1, col)
            dfs(grid_, row - 1, col)
            dfs(grid_, row, col + 1)
            dfs(grid_, row, col - 1)

        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    dfs(grid, r, c)
                    count += 1

        return count
