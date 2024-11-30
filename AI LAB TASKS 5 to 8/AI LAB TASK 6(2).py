def BFS(start,goalState): 
    if start not in visited:
        visited.append(start)
        if start==goalState:
            return
        for neighbour in tree[start]:
            BFS(neighbour,goalState)
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}
visited=[]
BFS('A','B')
print(visited)