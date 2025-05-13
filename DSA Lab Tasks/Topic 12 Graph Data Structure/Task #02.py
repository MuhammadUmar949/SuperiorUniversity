# Graph class definition
class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append((v, 1))  # Assuming weight of 1 for simplicity
        self.adj_list[v].append((u, 1))  # Assuming undirected graph

    # BFS and DFS Traversal
    def bfs(self, start):
        visited = set()
        queue = [start]
        result = []
        
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                for neighbor, _ in self.adj_list[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        return result
    
    def dfs(self, start):
        visited = set()
        result = []
        self._dfs_recursive(start, visited, result)
        return result
    
    def _dfs_recursive(self, vertex, visited, result):
        visited.add(vertex)
        result.append(vertex)
        for neighbor, _ in self.adj_list[vertex]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited, result)

# Test
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
print("BFS:", g.bfs(0))
print("DFS:", g.dfs(0))