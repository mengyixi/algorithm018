class Solution:
    @staticmethod
    def min_path_sum(grid):
        if not grid or not grid[0]:
            return 0

        dp = [float('inf')] * len(grid[0])
        dp[0] = 0
        # dp[1]是真正的起始点，前面没值，用+1替代-1，避免掉 -1超界的情况
        for row in grid:
            for index, num in enumerate(row):
                if index == 0:
                    dp[index] = dp[index] + num
                else:
                    dp[index] = min(dp[index], dp[index - 1]) + num
        return dp[-1]


test_cases = [
    {"input": [[1, 3, 1], [1, 5, 1], [4, 2, 1]], "expect": 7}
]

for case in test_cases:
    assert (Solution.min_path_sum(case['input']) is case['expect'])

print("pass!")
