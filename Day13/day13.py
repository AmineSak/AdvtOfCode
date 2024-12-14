from collections import defaultdict
import numpy as np

def get_input():
    res = []
    with open("input.txt") as f:
        for line in f:
            res.append(list(line.strip().split(",")))
    res = list(filter(lambda x: x != [''], res))
    machines = defaultdict(list)
    i = 0
    while i < len(res):
        M = np.zeros((2,2))
        for j in range(2):
            M[j] = list(map(int,res[i+j]))
        machines[i].append(M)
        machines[i].append(np.array(list(map(int,res[i+2]))))
        i += 3
    return machines

machines = get_input()

def solve(ax, ay, bx, by, px, py):  
    DP = {}
    def f(x,y):
        if (x,y) in DP:
            return DP[(x,y)]
        if x == 0 and y == 0:
            return 0
        if x < 0 or y < 0:
            return 10**9
        ans = min(3+f(x-ax,y-ay), 1+f(x-bx,y-by))
        DP[(x,y)] = ans
        return ans
    ans = f(px,py)
    if ans < 401:
        return ans
    else: 
        return 0

def solution1():
    # 3 to press A and 4 to press B
    ans = 0
    for m in machines.values():
        ax, ay, bx, by, px, py = m[0][0,0], m[0][0,1], m[0][1,0], m[0][1,1], m[1][0], m[1][1] 
        ans += solve(ax, ay, bx, by, px, py)
    return ans


def solution2():
    ans = 0
    for m in machines.values():
        ax, ay, bx, by, px, py = m[0][0,0], m[0][0,1], m[0][1,0], m[0][1,1], m[1][0], m[1][1] 
        px += 10000000000000
        py += 10000000000000
        x = (px*by - py*bx) / (ax*by - ay*bx)
        y = (px-ax*x) / bx
        if x %1 == y%1 == 0:
            ans += int(3 * x + y)

    return ans