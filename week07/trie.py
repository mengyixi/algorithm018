class Trie:
    """
    字典树
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tree = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        """
        tree = self.tree
        for letter in word:
            if letter not in tree:
                tree[letter] = {}
            tree = tree[letter]
        tree["$"] = "$"

    def search(self, word):
        """
        Returns if the word is in the trie.
        """
        tree = self.tree
        for letter in word:
            if letter not in tree:
                return False
            tree = tree[letter]
        if "$" in tree:
            return True
        return False

    def starts_with(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tree = self.tree
        for letter in prefix:
            if letter not in tree:
                return False
            tree = tree[letter]
        return True


test_cases = [
    {"input": "apple", "expect": None, "func": "insert"},
    {"input": "apple", "expect": True, "func": "search"},
    {"input": "app", "expect": False, "func": "search"},
    {"input": "app", "expect": True, "func": "starts_with"},
    {"input": "app", "expect": None, "func": "insert"},
    {"input": "app", "expect": True, "func": "search"},
]
tree = Trie()
for case in test_cases:
    _func = tree.__getattribute__(case['func'])
    assert (_func(case['input']) is case['expect'])

print("pass!")
