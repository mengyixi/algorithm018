class Solution:
    """
    leetcode 51.N皇后
    link: https://leetcode-cn.com/problems/n-queens/description/
    """
    @staticmethod
    def solve_n_queens(n):
        def generate_board():
            board = list()
            for i in range(n):
                row[queens[i]] = "Q"
                board.append("".join(row))
                row[queens[i]] = "."
            return board

        def solve(r, columns, diagonals1, diagonals2):
            if r == n:
                board = generate_board()
                output.append(board)
            else:
                available_positions = ((1 << n) - 1) & (~(columns | diagonals1 | diagonals2))
                while available_positions:
                    position = available_positions & (-available_positions)
                    available_positions = available_positions & (available_positions - 1)
                    column = bin(position - 1).count("1")
                    queens[r] = column
                    solve(r + 1, columns | position, (diagonals1 | position) << 1, (diagonals2 | position) >> 1)

        output = []
        queens = [-1] * n
        row = ["."] * n
        solve(0, 0, 0, 0)
        return output
