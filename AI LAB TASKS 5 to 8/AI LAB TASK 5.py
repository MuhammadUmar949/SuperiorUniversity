from collections import deque as d
def DFS(start,goalState):
    stack=d([start])
    while stack:
    currNode=stack.pop()
    if currNode not in visited:
    visited.append(currNode)
    if currNode==goalState:
        break
    for neighbour in reversed(tree[currNode]):
        stack.append(neighbour)
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
DFS('A','B')
print(visited)