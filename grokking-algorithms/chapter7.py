# Using an implementation of hashmaps for a graph
def create_paino_trading() -> dict:
    graph = {}
    graph['book'] = [('poster', 0), ('rareLp', 5)]
    graph['poster'] = [('drumSet', 35), ('bassGuitar', 20)]
    graph['rareLp'] = [('bassGuitar', 15), ('drumSet', 20)]
    graph['drumSet'] = [('piano', 10)]
    graph['bassGuitar'] = [('piano', 20)]
    graph['piano'] = []
    return graph

def create_exercise_A() -> dict:
    graph = {}
    graph['start'] = [('1', 5), ('2', 2)]
    graph['1'] = [('3', 4), ('4', 2)]
    graph['2'] = [('1', 8), ('4', 7)]
    graph['3'] = [('4', 6), ('fin', 3)]
    graph['4'] = [('fin', 1)]
    graph['fin'] = []
    return graph

def create_exercise_B() -> dict:
    graph = {}
    graph['start'] = [('1', 10)]
    graph['1'] = [('2', 20)]
    graph['2'] = [('fin', 30), ('3', 1)]
    graph['3'] = [('1', 1)]
    graph['fin'] = []
    return graph

def create_exercise_C() -> dict:
    graph = {}
    graph['start'] = [('1', 2), ('2', 2)]
    graph['1'] = [('3', 2), ('fin', 2)]
    graph['2'] = [('1', 2)]
    graph['3'] = [('2', -1), ('fin', 2)]
    graph['fin'] = []
    return graph

def get_value(t: tuple):
    return t[1]

def djikstra(graph: dict, start: str, dst: str) -> (str, int):
    nodes = dict.fromkeys(graph.keys(), ('parent key', float('inf')))
    looked_at = {start}
    for node in graph[start]:
        nodes[node[0]] = (start, node[1])
    while len(looked_at) < len(nodes):
        # Get next minimal node
        costs = [(k, v[1]) for k, v in nodes.items() if k not in looked_at]
        costs.sort(key=get_value)
        curr_key = costs[0][0]
        neighbors = graph[curr_key]
        # check neighbors of minimal node
        for n in neighbors:
            if nodes[curr_key][1] + n[1] <  nodes[n[0]][1]:
                nodes[n[0]] = (curr_key, nodes[curr_key][1] + n[1])
        looked_at.add(curr_key)
    # construct path
    path = dst
    prev = nodes[dst]
    while prev[0] != start and prev[0] != 'parent key':
        path = prev[0] + ' -> ' + path
        prev = nodes[prev[0]]
    path = start + ' -> '  + path
    return path, nodes[dst][1]

def print_djikstra(graph: dict, start: str, dst: str):
    print(f'Searching for {dst} starting from {start}')
    path, cost = djikstra(graph, start, dst)
    print(f'Going to {dst} via {path}\nCosts only {cost}')

if __name__ == '__main__':
    # print('Piano Trading')
    # print_djikstra(create_paino_trading(), 'book', 'piano')
    print('Excersise A')
    print_djikstra(create_exercise_A(), 'start', 'fin')
    print('Excersise B')
    print_djikstra(create_exercise_B(), 'start', 'fin')
    print('Excersise C')
    print_djikstra(create_exercise_C(), 'start', 'fin')