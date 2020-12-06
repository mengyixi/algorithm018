class Solution:
    @staticmethod
    def find_words(board, words):
        _key = '$'

        trie = {}
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            node[_key] = word

        row_count = len(board)
        col_count = len(board[0])

        matched_words = []

        def backtracking(row, col, parent):
            letter = board[row][col]
            curr_node = parent[letter]
            word_match = curr_node.pop(_key, False)

            if word_match:
                matched_words.append(word_match)

            board[row][col] = '#'

            for (row_offset, col_offset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                new_row, new_col = row + row_offset, col + col_offset
                if new_row < 0 or new_row >= row_count or new_col < 0 or new_col >= col_count:
                    continue
                if not board[new_row][new_col] in curr_node:
                    continue
                backtracking(new_row, new_col, curr_node)

            board[row][col] = letter

            if not curr_node:
                parent.pop(letter)

        for row in range(row_count):
            for col in range(col_count):
                if board[row][col] in trie:
                    backtracking(row, col, trie)

        return matched_words


test_cases = [
    {
        "input": {
            "board": [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
            "words": ["oath", "pea", "eat", "rain"]
        },
        "expect": ["oath", "eat"]
    }, {
        "input": {
            "board": [["a", "b"], ["c", "d"]],
            "words": ["abcb"]
        },
        "expect": []
    }
]

for case in test_cases:
    assert (Solution.find_words(case['input']['board'], case['input']['words']) == case['expect'])

print("pass!")
