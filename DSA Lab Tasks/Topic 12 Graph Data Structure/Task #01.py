# Graph Representation
class Graph:
    def __init__(self, directed=False):
        self.adj_list = {}
        self.adj_matrix = []
        self.vertices = []
        self.directed = directed
    
    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            self.vertices.append(vertex)
            # Update adjacency matrix
            for row in self.adj_matrix:
                row.append(0)
            self.adj_matrix.append([0] * len(self.vertices))
    
    def add_edge(self, v1, v2, weight=1):
        if v1 not in self.adj_list:
            self.add_vertex(v1)
        if v2 not in self.adj_list:
            self.add_vertex(v2)
        
        self.adj_list[v1].append((v2, weight))
        v1_index = self.vertices.index(v1)
        v2_index = self.vertices.index(v2)
        self.adj_matrix[v1_index][v2_index] = weight
        
        if not self.directed:
            self.adj_list[v2].append((v1, weight))
            self.adj_matrix[v2_index][v1_index] = weight
    
    def display_adj_list(self):
        print("Adjacency List:")
        for vertex in self.adj_list:
            print(f"{vertex}: {self.adj_list[vertex]}")
    
    def display_adj_matrix(self):
        print("Adjacency Matrix:")
        print("   ", " ".join(self.vertices))
        for i, row in enumerate(self.adj_matrix):
            print(f"{self.vertices[i]}: {row}")

# Test
g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_edge("A", "B")
g.display_adj_list()
g.display_adj_matrix()