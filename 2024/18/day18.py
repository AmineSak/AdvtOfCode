from collections import deque

def get_input(filename):
    res = []
    with open(filename) as f :
        for line in f:
            res.append(list(map(int,line.strip().split(","))))
    return res

coords = get_input("input.txt")
row = col = 71

grid = [["." for _ in range(col) ] for _ in range(row)]

target = (70,70)

dirs = [(-1,0), (0,1), (1,0), (0,-1)]

for i,j in coords:
    grid[j][i] = "#"
    stack = deque([(0,0)])
    seen = {(0,0)}
    reachable = False
    while stack:
        r, c = stack.popleft()

        if (r,c) == target:
            reachable = True
            break
        
        for dr,dc in dirs:
            nr, nc = r+dr, c+dc
            
            if not 0<= nr<row:continue
            if not 0<= nc<col:continue

            if (nr,nc) not in seen and grid[nr][nc] != "#":
                stack.append((nr,nc))
                seen.add((nr,nc))
        
    if not reachable:
        print("solultion 2: ",(i,j))
        break
        