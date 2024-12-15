import networkx as nx
import matplotlib.pyplot as plt

def get_lists():
    # Open the file in read mode
    with open("lists.txt", "r") as f:
        res = []  
        for line in f:
            l = list(map(int,list(line.strip().split(","))))
            res.append(l)
    return res
    

def get_rules():
    # Open the file in read mode
    with open("rules.txt", "r") as f:
        res = []  
        for line in f:
            X, Y = list(line.strip().split())
            res.append([int(X), int(Y)])
    return res
def to_graph(rules):
    nodes = set()
    m = 0
    for X,Y in rules:
        m = max(max(m, X), Y)
        nodes.add(X)
        nodes.add(Y)
    G = [[] for _ in range(m + 1)]

    for X, Y in rules:
        G[X].append(Y)
    
    return G

def bfs(l,rules_graph):
    ans = 0
    start_ind = 0
    end = len(l) - 1

    stack =[l[start_ind]]
    while stack:
        current = stack.pop()
        if start_ind == end:
            ans += l[end // 2]
            break
        start_ind += 1
        neighbors = rules_graph[current]
        for neighbor in neighbors:
            if neighbor == l[start_ind]:
                stack.append(neighbor) 
    return ans

rules = get_rules()
lists = get_lists()
G = to_graph(rules)


def solution1(rules_graph):
    ans = 0
    lists_c = lists.copy()
    for l in lists_c:
        m = bfs(l,rules_graph)
        if m > 0:
            ans += m
            lists.remove(l)

    return ans


def solution2(lists , rules_graph):
    ans = 0
    for l in lists:
        changed = True
        while changed:
            changed = False
            for i in range(len(l) - 1):
                a = l[i]
                b = l[i+1]
                if b in rules_graph[a]:
                    l[i] , l[i+1] = l[i+1], l[i]
                    changed =True

        ans += l[(len(l) - 1) // 2]

    return ans


def show_graph():
    g = nx.Graph()
    for i, neighbors in enumerate(G):
        for neighbor in neighbors:
            g.add_edge(i, neighbor)

    # Draw the graph
    nx.draw(g, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
    plt.show()