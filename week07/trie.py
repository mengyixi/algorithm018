class Trie:
    """
    字典树
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        """
        node = self.root
        for letter in word:
            node = node.setdefault(letter, {})
        node["$"] = "$"

    def search(self, word):
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for letter in word:
            if letter not in node:
                return False
            node = node[letter]
        return "$" in node

    def starts_with(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for letter in prefix:
            if letter not in node:
                return False
            node = node[letter]
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
