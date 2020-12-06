学习笔记
trie树代码模板(python版)
```python
class Trie:
  
	def __init__(self): 
		self.root = {} 
		self.end_of_word = "#" 
 
	def insert(self, word): 
		node = self.root 
		for char in word: 
			node = node.setdefault(char, {}) 
		node[self.end_of_word] = self.end_of_word 
 
	def search(self, word): 
		node = self.root 
		for char in word: 
			if char not in node: 
				return False 
			node = node[char] 
		return self.end_of_word in node 
 
	def starts_with(self, prefix): 
		node = self.root 
		for char in prefix: 
			if char not in node: 
				return False 
			node = node[char] 
		return True
```
并查集代码模板(python版)
```python
class UnionFind:
    p = []

    def init(self, n): 
        self.p = [i for i in range(n)] 
 
    def union(self, i, j): 
        p1 = self.find(i) 
        p2 = self.find(j) 
        self.p[p1] = p2 
     
    def find(self, i): 
        root = i 
        while self.p[root] != root: 
            root =self.p[root] 
        while self.p[i] != i:
            x = i; i = self.p[i]; self.p[x] = root 
        return root
```
双向BFS
```python
def bfs(g, start, end):
    left_visited = set()
    left_visited.add(start)
    right_visited = set()
    right_visited.add(end)
    left_queue = [start]
    right_queue = [end]

    while left_queue and right_queue:
        for i in range(len(left_queue)):
            node = left_queue.pop()
            left_visited.add(node)
            assert (node in right_visited)
            # process

        for i in range(len(right_queue)):
           node = right_queue.pop()
           right_visited.add(node)
           assert (node in left_visited)
           # process
```