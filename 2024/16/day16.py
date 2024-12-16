import numpy as np
import heapq
from collections import deque

def get_char_matrix(filename):
    with open (filename, 'r') as f:
        res = []
        for line in f:
            row = np.array(list(line.strip()))
            res.append(row)
        res = np.array(res)
    return res
grid = get_char_matrix("input.txt")

row = len(grid)
col = len(grid[0])

sr, sc = 0,0



for i in range(row):
    for j in range(col):
        if grid[i,j] == "S":
            sr, sc = i,j
    

pq = [(0,sr,sc,0,1)]
lowest_cost = {(sr,sc,0,1):0}
backtrack = {}
best_cost = float("inf")
end_states = set()

while pq:
    cost, r, c, dr,dc = heapq.heappop(pq)
    if lowest_cost.get((r,c,dr,dc),float("inf")) < cost: continue
    if grid[r,c] == "E":
        if cost > best_cost: break
        best_cost = cost
        end_states.add((r,c,dr,dc))
    for  new_cost, nr, nc, ndr, ndc in [(cost + 1,r+dr,c+dc, dr,dc) , (cost+1000, r,c,dc,-dr),(cost+1000, r,c,-dc,dr)]:
        if grid[nr,nc] == "#": continue
        lowest = lowest_cost.get((nr,nc,ndr,ndc) , float("inf"))
        if new_cost > lowest:continue
        if new_cost < lowest:
            backtrack[(nr,nc,ndr,ndc)] = set()
            lowest_cost[(nr,nc,ndr,ndc)] = new_cost
        backtrack[(nr,nc,ndr,ndc)].add((r,c,dr,dc))
        heapq.heappush(pq,(new_cost,nr,nc,ndr,ndc))

states = deque(end_states)
seen = set(end_states)

while states:
    key = states.popleft()
    for last in backtrack.get(key,[]):
        if last in seen:continue
        seen.add(last)
        states.append(last)

print(len({(r,c) for r,c,_,_ in seen}))




