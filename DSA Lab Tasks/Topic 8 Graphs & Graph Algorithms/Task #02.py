# Implementing BFS and DFS
from collections import deque

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {i: [] for i in range(vertices)}

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

class GraphTraversal(Graph):
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        result = []
        
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                result.append(node)
                queue.extend(self.adj_list[node])
        return result
    
    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        result = [start]
        for neighbor in self.adj_list[start]:
            if neighbor not in visited:
                result.extend(self.dfs(neighbor, visited))
        return result

# Example usage:
g = GraphTraversal(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
print(g.bfs(0))  # Output: [0, 1, 2, 3, 4, 5]
print(g.dfs(0))  # Output: [0, 2, 5, 1, 4, 3]
