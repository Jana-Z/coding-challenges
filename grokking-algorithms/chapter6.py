class Node:

    def __init__(self, value, nexts):
        self.nexts = nexts
        self.value = value

    def get_nexts(self):
        return self.nexts

    def get_value(self):
        return self.value

def create_graph_6_1():
    # Connection in graph:
    #       s -> n1 -> f
    #       s -> n2 -> n4 -> f
    #       n2 -> n3 || n1 -> n3
    finish = Node("finish", [])
    n3 = Node(None, [])
    n4 = Node(None, [finish])
    n1 = Node(None, [finish, n3])
    n2 = Node(None, [n3, n4])
    start = Node(None, [n1, n2])
    return start

def create_graph_6_2():
    bat = Node("bat", [])
    mat = Node("mat", [bat])
    cat = Node("cat", [bat, mat])
    bar = Node("bar", [bat])
    car = Node("car", [bar, cat])
    cab = Node("cab", [car, cat])
    return cab

def breadth_first_search(start, searchkey):
    queue = [(start, 0)]
    queue.extend([(s, 1) for s in start.get_nexts()])
    already_checked = {p[0] for p in queue}
    while queue:
        curr_node = queue.pop(0)
        if curr_node[0].get_value() == searchkey:
            return curr_node[1]
        else:
            for n in curr_node[0].get_nexts():
                if n not in already_checked:
                    queue.append((n, curr_node[1] + 1))
                else:
                    already_checked.add(n)
    return -1

def print_bfs(start, searchkey):
    print(f'Seaching in the graph for {searchkey}')
    res = breadth_first_search(start, searchkey)
    if res != -1:
        print(f'Found at degree {res}')
    else:
        print('Not found')

if __name__ == "__main__":
    print(f'Creating the graph for exercise 6.1')
    start = create_graph_6_1()
    print_bfs(start, "finish")
    print_bfs(start, "Not in there")
    print(f'Creating the graph for exercise 6.2')
    start = create_graph_6_2()
    print_bfs(start, "Not in there")
    print_bfs(start, "bat")