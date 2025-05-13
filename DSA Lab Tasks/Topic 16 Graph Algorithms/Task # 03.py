#  Cycle Detection
def detect_cycle_undirected(graph):
    visited = set()
    
    def has_cycle(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if has_cycle(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False
    
    for node in graph:
        if node not in visited:
            if has_cycle(node, None):
                return True
    return False

def detect_cycle_directed(graph):
    visited = set()
    recursion_stack = set()
    
    def has_cycle(node):
        visited.add(node)
        recursion_stack.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if has_cycle(neighbor):
                    return True
            elif neighbor in recursion_stack:
                return True
        recursion_stack.remove(node)
        return False
    
    for node in graph:
        if node not in visited:
            if has_cycle(node):
                return True
    return False

# Test
undirected_graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D'},
    'C': {'A', 'D'},
    'D': {'B', 'C'}
}

directed_graph = {
    'A': {'B'},
    'B': {'C'},
    'C': {'A'}
}

print("Undirected graph has cycle:", detect_cycle_undirected(undirected_graph))
print("Directed graph has cycle:", detect_cycle_directed(directed_graph))