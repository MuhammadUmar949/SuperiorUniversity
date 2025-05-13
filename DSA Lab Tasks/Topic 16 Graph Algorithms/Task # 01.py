# DFS and BFS Traversal
def dfs(graph, start):
    visited = set()
    result = []
    
    def helper(vertex):
        visited.add(vertex)
        result.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                helper(neighbor)
    
    helper(start)
    return result

def bfs(graph, start):
    visited = set([start])
    queue = [start]
    result = []
    
    while queue:
        vertex = queue.pop(0)
        result.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return result

# Test
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("DFS:", dfs(graph, 'A'))
print("BFS:", bfs(graph, 'A'))