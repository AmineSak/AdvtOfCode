from collections import defaultdict

graph = defaultdict(set)
for line in open("input.txt").read().splitlines():
    a,b = line.split("-")
    graph[a].add(b)
    graph[b].add(a)
sets = set()
def search(node,req):
    key = tuple(sorted(req))
    if key in sets: return
    sets.add(key)
    for neighbor in graph[node]:
        if neighbor in req: continue
        if not req <= graph[neighbor] : continue
        search(neighbor, req | {neighbor})

for node in graph:
    search(node,{node})

print(",".join(max(sets,key=len)))
        


triple_connexions = set()
for node0 in graph:
    for node1 in graph[node0]:
        for node2 in graph[node1]:
            if node0 != node2 and node0 in graph[node2]:
                triple_connexions.add(tuple(sorted([node0,node1,node2])))
                

print(len([tc for tc in triple_connexions if any(c.startswith("t") for c in tc)]))
    