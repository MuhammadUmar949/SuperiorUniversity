class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0
    def __eq__(self, other):
        return self.state == other.state
def A_Asteric(startState, goalState, heuristicFunction, tree):
    startNode = Node(startState)
    goalNode = Node(goalState)
    openList = [startNode]
    closedList = []
    while openList:
        currentNode = min(openList, key=lambda x: x.f)
        if currentNode.state == goalNode.state:
            path = []
            cost = currentNode.g
            while currentNode:
                path.append(currentNode.state)
                currentNode = currentNode.parent
            return path[::-1], cost
        openList.remove(currentNode)
        closedList.append(currentNode)
        neighbors = tree.get(currentNode.state, [])
        for neighborState, moveCost in neighbors:
            neighborNode = Node(neighborState, currentNode)
            if neighborNode in closedList:
                continue
            tentativeG = currentNode.g + moveCost
            neighborNode.h = heuristicFunction(neighborState, goalState)
            neighborNode.f = tentativeG + neighborNode.h
            if addToOpen(openList, neighborNode, tentativeG):
                neighborNode.g = tentativeG
                openList.append(neighborNode)
    return None, None
def addToOpen(openList, neighbor, tentativeG):
    for node in openList:
        if neighbor == node and tentativeG >= node.g:
            return False
    return True
def heuristicFunction(state, goalState):
    return 0

tree = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 5), ('E', 1)],
    'C': [('F', 3)],
    'D': [],
    'E': [('G', 2)],
    'F': [],
    'G': []
}
if __name__ == "__main__":
    startState = 'A'
    goalState = 'G'
    path, cost = A_Asteric(startState, goalState, heuristicFunction, tree)
    print("Our Path is ", path)
    print("Total cost:", cost)