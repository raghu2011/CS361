from collections import deque
import random
class Node:
    def __init__(self, state, parent=None):
        self.state=state
        self.parent=parent
def get_successors(node):
    successors=[]
    index =node.state.index(0)
    quotient =index // 3
    remainder= index % 3
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
            successors.append(Node(newstate, node))
    return successors
def bfs(start_state, goal_state):
    start_node=Node(start_state)
    queue=deque([start_node])
    visited=set()
    nodes_explored=0
    while queue:
        node=queue.popleft()
        if tuple(node.state) in visited:
            continue
        visited.add(tuple(node.state))
        nodes_explored += 1
        if node.state == goal_state:
            path=[]
            while node:
                path.append(node.state)
                node=node.parent
            print('Nodes explored:', nodes_explored)
            return path[::-1]

        for successor in get_successors(node):
            queue.append(successor)
    return None
start_state=[1, 2, 3, 4, 5, 6, 7, 8, 0]
s_node=Node(start_state)
D=20
d=0
while d <= D:
    goal_state=random.choice(list(get_successors(s_node))).state
    s_node=Node(goal_state)
    d += 1
solution=bfs(start_state, goal_state)
if solution:
    for step in solution:
        print(step)
else:
    print("No solution found.")