import heapq
import random
class Node:
    def __init__(self, state, parent=None, g=0, h=0):
        self.state=state
        self.parent=parent
        self.g=g
        self.h=h
        self.f=g + h
    def __lt__(self, other):
        return self.g < other.g
def heuristic(node, goal_state):
    return 0
def get_successors(node):
    successors=[]
    index=node.state.index(0)
    quotient=index // 3
    remainder=index % 3
    moves=[]
    if quotient == 0:
        moves=[3]
    if quotient == 1:
        moves=[-3, 3]
    if quotient == 2:
        moves=[-3]
    if remainder == 0:
        moves += [1]
    if remainder == 1:
        moves += [-1, 1]
    if remainder == 2:
        moves += [-1]
    for move in moves:
        im=index + move
        if 0 <= im < 9:
            newstate=list(node.state)
            newstate[index], newstate[im]=newstate[im], newstate[index]
            successors.append(Node(newstate, node, node.g + 1))
    return successors
def search_agent(start_state, goal_state):
    start_node=Node(start_state)
    frontier=[]
    heapq.heappush(frontier, (start_node.g, start_node))
    visited=set()
    while frontier:
        _, node=heapq.heappop(frontier)
        if tuple(node.state) in visited:
            continue
        visited.add(tuple(node.state))
        if node.state == goal_state:
            path=[]
            while node:
                path.append(node.state)
                node=node.parent
            return path[::-1]
        for successor in get_successors(node):
            heapq.heappush(frontier, (successor.g, successor))
    return None
start_state=[1, 2, 3, 4, 5, 6, 7, 8, 0]
s_node=Node(start_state)
D=20
d=0
while d <= D:
    goal_state=random.choice(list(get_successors(s_node))).state
    s_node=Node(goal_state)
    d += 1
solution=search_agent(start_state, goal_state)
if solution:
    for step in solution:
        print(step)
else:
    print("No solution found.")