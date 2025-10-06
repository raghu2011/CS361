initial_state = [1, 1, 1, 0, 2, 2, 2]
goal_state = [2, 2, 2, 0, 1, 1, 1]
def pick_R1(current_state, i):
    temp = current_state.copy()
    temp[i + 1] = 0
    temp[i] = 2
    return temp
def pick_R2(current_state, i):
    temp = current_state.copy()
    temp[i + 2] = 0
    temp[i] = 2
    return temp
def pick_L1(current_state, i):
    temp = current_state.copy()
    temp[i - 1] = 0
    temp[i] = 1
    return temp
def pick_L2(current_state, i):
    temp = current_state.copy()
    temp[i - 2] = 0
    temp[i] = 1
    return temp
def actions(current_state):
    possible_states = []
    i = current_state.index(0)
    if i == 0:
        if current_state[i + 1] == 2:
            possible_states.append(pick_R1(current_state, i))
        if current_state[i + 2] == 2:
            possible_states.append(pick_R2(current_state, i))
    elif i == 1:
        if current_state[i - 1] == 1:
            possible_states.append(pick_L1(current_state, i))
        if current_state[i + 1] == 2:
            possible_states.append(pick_R1(current_state, i))
        if current_state[i + 2] == 2:
            possible_states.append(pick_R2(current_state, i))
    elif 2 <= i < len(current_state) - 2:
        if current_state[i - 2] == 1:
            possible_states.append(pick_L2(current_state, i))
        if current_state[i - 1] == 1:
            possible_states.append(pick_L1(current_state, i))
        if current_state[i + 1] == 2:
            possible_states.append(pick_R1(current_state, i))
        if current_state[i + 2] == 2:
            possible_states.append(pick_R2(current_state, i))
    elif i == len(current_state) - 2:
        if current_state[i + 1] == 2:
            possible_states.append(pick_R1(current_state, i))
        if current_state[i - 1] == 1:
            possible_states.append(pick_L1(current_state, i))
        if current_state[i - 2] == 1:
            possible_states.append(pick_L2(current_state, i))
    elif i == len(current_state) - 1:
        if current_state[i - 1] == 1:
            possible_states.append(pick_L1(current_state, i))
        if current_state[i - 2] == 1:
            possible_states.append(pick_L2(current_state, i))

    return possible_states
class node:
    def __init__(self, state, parent, path_cost):
        self.state = state
        self.parent = parent
        self.path_cost = path_cost
class Frontier:
    def __init__(self, root_node):
        self.list_nodes = [root_node]
    def pop(self):
        if len(self.list_nodes) == 0:
            return "NotFound"
        first = self.list_nodes[0]
        self.list_nodes = self.list_nodes[1:].copy()
        return first
    def remove(self, nod):
        if nod not in self.list_nodes:
            return "NotFound"
        del self.list_nodes[self.list_nodes.index(nod)]
    def isbetter(self, nod):
        listsamestate = []
        for no in self.list_nodes:
            if nod.state == no.state:
                listsamestate.append(no)
        for no in listsamestate:
            if no.path_cost <= nod.path_cost:
                return False
        return True
    def top(self):
        if len(self.list_nodes) == 0:
            return "NotFound"
        my_node = self.list_nodes[0]
        cost = my_node.path_cost
        for nod in self.list_nodes:
            if nod.path_cost < cost:
                my_node = nod
        return my_node
    def is_empty(self):
        return len(self.list_nodes) == 0
    def add(self, nod):
        self.list_nodes.append(nod)
class Visited:
    def __init__(self):
        self.visited_list = []
    def add(self, nod):
        self.visited_list.append(nod)

    def isin(self, st):
        for no in self.visited_list:
            if st == no.state:
                return True
        return False
def backtrack(myfrontire, myvisited, top_node, home_state):
    currentnode = top_node
    while currentnode.state != home_state:
        print(currentnode.state)
        p = currentnode.parent
        for no in myvisited.visited_list:
            if no.state == p:
                currentnode = no
    print(currentnode.state)
def bfs_agent(initial_state, goal_state):
    home_state = initial_state.copy()
    parent_node = node(initial_state, None, 0)
    myfrontire = Frontier(parent_node)
    myvisited = Visited()

    if initial_state == goal_state:
        print(initial_state)
        return initial_state
    while not myfrontire.is_empty():
        top_node = myfrontire.top()
        myfrontire.remove(top_node)
        if top_node.state == goal_state:
            print(top_node.state)  # Print the goal state
            return top_node.state
        if myvisited.isin(top_node.state):
            continue

        myvisited.add(top_node)
        print(top_node.state)  # Print the current state
        all_possible_actions = actions(top_node.state)
        c = top_node.path_cost
        all_possible_nodes = [
            node(st, top_node.state, c + 1) for st in all_possible_actions
        ]
        cleannodes = []
        for no in all_possible_nodes:
            if myfrontire.isbetter(no) and not myvisited.isin(no.state):
                cleannodes.append(no)
            if myfrontire.isbetter(no):
                myfrontire.remove(no)
        for no in cleannodes:
            myfrontire.add(no)
if __name__ == "__main__":
    initial_state = [1, 1, 1, 0, 2, 2, 2]
    goal_state = [2, 2, 2, 0, 1, 1, 1]
    print("=" * 79)
    print("=" * 30, end="")
    print("Rabbit Leap", end="")
    print("=" * 35, end="\n\n")
    bfs_agent(initial_state, goal_state)
    print("=" * 36, end="")
    print("End", end="")
    print("=" * 40, end="\n\n")
