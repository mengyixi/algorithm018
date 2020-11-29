import bisect


class Solution:
    @staticmethod
    def max_sum_sub_matrix(matrix, k):
        row, col = len(matrix), len(matrix[0])
        res = float('-inf')

        for left in range(col):
            nums = [0] * row
            for right in range(left, col):
                for i in range(row):
                    nums[i] += matrix[i][right]
                array = [0]
                cum = 0
                for num in nums:
                    cum += num
                    loc = bisect.bisect_left(array, cum - k)
                    if loc < len(array):
                        res = max(res, cum - array[loc])
                    bisect.insort(array, cum)
        return res


test_cases = [
    {"input": {"matrix": [[1, 3, 1], [1, 5, 1], [4, 2, 1]], "k": 2}, "expect": 2}
]

for case in test_cases:
    assert (Solution.max_sum_sub_matrix(case['input']['matrix'], case['input']['k']) is case['expect'])

print("pass!")
