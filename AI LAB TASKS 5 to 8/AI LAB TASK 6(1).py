from collections import deque as d
def BFS(start,goalState): 
    Queue=d([start])
    while Queue:
    currNode=Queue.popleft()
    if currNode not in visited:
        visited.append(currNode)
        if currNode==goalState:
            return
        for neighbour in tree[currNode]:
        if neighbour not in visited:
            Queue.append(neighbour)
            
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