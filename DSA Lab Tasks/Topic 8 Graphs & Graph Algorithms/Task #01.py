# Implementing a Graph Using Adjacency List & Adjacency Matrix
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {i: [] for i in range(vertices)}
        self.adj_matrix = [[0] * vertices for _ in range(vertices)]
    
    def add_edge(self, v1, v2):
        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)
        self.adj_matrix[v1][v2] = 1
        self.adj_matrix[v2][v1] = 1
    
    def display(self):
        print("Adjacency List:")
        for key, value in self.adj_list.items():
            print(f"{key}: {value}")
        
        print("\nAdjacency Matrix:")
        for row in self.adj_matrix:
            print(row)

# Example usage:
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.display()
