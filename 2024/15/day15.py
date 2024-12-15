import numpy as np

def get_char_matrix(filename):
    with open (filename, 'r') as f:
        grid, movements = f.read().split("\n\n")
        grid = grid.splitlines()
        movements = movements.strip()
        M = [np.array(list(line.strip())) for line in grid]
        M = np.array(M)
    return M, "".join(movements.split())

M, movements =  get_char_matrix("input.txt")

row = len(M)
col = len(M[0])

def wall(i,j):
    return M[i,j] == "#"

def find_robot():
    for i in range(row):
        for j in range(col):
            if M[i,j] == "@":
                return i, j
            


i, j = find_robot()
dirs = {"^":(-1,0) , "v":(1,0), ">":(0,1), "<":(0,-1)}
def move(pos,dir):
    i,j = pos
    crates = 0
    dir1, dir2 = dirs[dir][0] , dirs[dir][1]
    if M[i+dir1, j+dir2] == ".":
        M[i,j] = "."
        i,j = i+dir1, j+dir2
        M[i,j] = "@"
        return i,j
    
    if M[i+dir1, j+dir2] == "#":
        return pos
    
    while M[i+dir1, j+dir2] == "O":
        crates += 1
        i,j = i+dir1, j+dir2
    if M[i+dir1, j+dir2] == ".":
        k = 0
        while k < crates:
            k +=1
            M[i+dir1,j+dir2] = "O"
            M[i,j] = "."
            i,j = i-dir1, j-dir2
        M[i,j] = "."
        M[i+dir1,j+dir2] = "@"
        return i+dir1,j+dir2
    if M[i+dir1, j+dir2] == "#":
        return pos


        
def solution1():
    ans = 0
    new_pos = find_robot()
    for m in movements:
        new_pos = move(new_pos, m)
    for i in range(row):
        for j in range(col):
            if M[i,j] == "O":
                ans += i*100 + j

    return ans

M2 = []
for l in M:
    r=[]
    for p in l:
        if p == "#":
            r.append("#")
            r.append("#")
        if p == ".":
            r.append(".")
            r.append(".")
        if p == "O":
            r.append("[")
            r.append("]")
        if p == "@":
            r.append("@")    
            r.append(".")
    M2.append(r)
M2 = np.array(M2)

def find_robot2():
    for i in range(row):
        for j in range(col):
            if M2[i,j] == "@":
                return i, j

def move2(pos,dir):
    i, j = pos
    dir1, dir2 = dirs[dir][0] , dirs[dir][1]
    targets = [(i,j)]
    go = True
    for cr,cc in targets:
        nr, nc = cr + dir1, cc + dir2
        if (nr,nc) in targets: continue
        char = M2[nr,nc]
        if char == "#":
            go = False
            break
        if char == "[":
            targets.append((nr,nc+1))
            targets.append((nr,nc))
        if char == "]":
            targets.append((nr,nc))
            targets.append((nr,nc-1))
    if go:
        copy = [list(row) for row in M2]
        M2[i,j] = "."
        for br,bc in targets[1:]:
            M2[br,bc] = "."
        for br,bc in targets[1:]:
            M2[ br+dir1 , bc+dir2] = copy[br][bc]
        return i+dir1,j+dir2
    return pos

def solution2():
    ans = 0
    new_pos = find_robot2()
    for m in movements:
        new_pos = move2(new_pos, m)
    for i in range(len(M2)):
        for j in range(len(M2[0])):
            if M2[i,j] == "[":
                ans += i*100 + j

    return ans

