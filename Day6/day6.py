import numpy as np
import time

def get_matrix():

    with open ('input.txt', 'r') as f:
        res = []
        for line in f:
            row = np.array(list(line.strip()))
            res.append(row)
        res = np.array(res)

    return res

M = get_matrix()
row = len(M)
col = len(M[1])

dirs = [(-1,0) , (0, 1) , (1,0), (0,-1)]

def find_guard(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] == "^":
                M[i,j] = "."  # Find the guard's starting position
                return i, j



x , y = find_guard(M)
start_dir = 0
start_pos = (x,y) 

def solve_cycle():
    states = set()
    start_dir = 0
    x, y = start_pos
    while(True):
        if (x ,y, dirs[start_dir]) in states:
            return True
        states.add((x, y,dirs[start_dir]))
        x1 = x + dirs[start_dir][0]
        y1 = y + dirs[start_dir][1]
        if not(x1 >= 0 and x1 < row and y1 < col and y1 >= 0):
            return False
        if M[x1,y1] == ".":
            x , y = x1, y1
        else:
            start_dir = (start_dir + 1) % 4


# Part I
hset = set()
while(True):
    x1 = x + dirs[start_dir][0]
    y1 = y + dirs[start_dir][1]
    if not(x1 >= 0 and x1 < row and y1 < col and y1 >= 0):
        break
    if M[x1,y1] == ".":
        x , y = x1, y1
        hset.add((x,y))
    else:
        start_dir = (start_dir + 1) % 4

# Part II
t0 = time.time()
ans = 0
for i in range(row):
    for j in range(col):
        if M[i,j] == "." and [i,j] != [x,y]:
            M[i,j] = "#"

            if solve_cycle():
                ans += 1            

            M[i,j] = "."
t1 = time.time()
print("Part I:" + f"{len(hset)} ")
print("Part II:" + f"{ans}, elapsed: f'{t1 -t0}'")





