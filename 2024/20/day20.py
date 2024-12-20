import numpy as np
from collections import deque, defaultdict
import heapq as hq

def get_char_matrix(filename):
    with open (filename, 'r') as f:
        res = []
        for line in f:
            row = np.array(list(line.strip()))
            res.append(row)
        res = np.array(res)
    return res

grid = get_char_matrix("input.txt")

rows = len(grid)
cols = len(grid[0])

dirs = [(-1,0), (1,0), (0,-1), (0,1)]

# find S
for i in range(rows):
    for j in range(cols):
        if grid[i,j] == "S":
            sr,sc = i,j


# get the distance grid 
dists = [[-1 for _ in range(cols)] for _ in range(rows) ]
dists = np.array(dists)
dists[sr,sc] = 0

while grid[sr,sc] != "E":
    for dr,dc in dirs:
        nr,nc = sr+dr, sc+dc
        if not 0<= nr< rows: continue
        if not 0<= nc< cols: continue
        if grid[nr,nc] == "#": continue
        if dists[nr,nc] != -1: continue
        dists[nr,nc] = dists[sr,sc] + 1
        sr=nr
        sc=nc
count = 0
for r in range(rows):
    for c in range(cols):
        if dists[r,c] == -1: continue
        for k in range(2,21):
            for dr in range(k + 1):
                dc = k - dr
                for nr,nc in {(r+dr,c+dc), (r+dr,c-dc), (r-dr,c-dc),(r-dr,c+dc)}:
                    if not 0<= nr< rows: continue
                    if not 0<= nc< cols: continue
                    if grid[nr,nc] == "#": continue
                    if dists[nr,nc] - dists[r,c] >= k+100: count += 1
            

print(count)