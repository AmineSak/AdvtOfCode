import numpy as np
from collections import defaultdict

def get_matrix():
    with open ('input.txt', 'r') as f:
        res = []
        for line in f:
            row = np.array(list(map(int,list(line.strip()))))
            res.append(row)
        res = np.array(res)
    return res

M = get_matrix()
row = len(M)
col = len(M[2])


def inbounds(i ,j ):
    return 0<= i < row and  0<= j < col

def toGraph():
    G = defaultdict(list)
    for i in range(row):
        for j in range(col):
            left = (i,j-1)
            right = (i,j+1)
            top = (i-1,j)
            down = (i+1,j)
            if inbounds(*left):
                G[(i,j)].append(left)
            if inbounds(*right):
                G[(i,j)].append(right)
            if inbounds(*top):
                G[(i,j)].append(top)
            if inbounds(*down):
                G[(i,j)].append(down)
    return G
G = toGraph()


def BFS_score(G,start_node: tuple):
    score = 0
    stack = []
    visited_nines = set()
    stack.append(start_node)

    while stack:
        current_node_coords = stack.pop()
        current_val = M[current_node_coords]
        
        if current_val == 9:
            if current_node_coords not in visited_nines:
                score += 1 
                visited_nines.add(current_node_coords)

        neighbors = G[current_node_coords]
        for neighbor in neighbors:
            if M[neighbor] == current_val + 1 and M[neighbor] <= 9:
                stack.append(neighbor)
    return score

def BFS_ratings(G, start_node: tuple):
    ratings = 0
    stack = []
    stack.append(start_node)

    while stack:
        current_node_coords = stack.pop()
        current_val = M[current_node_coords]
        
        if current_val == 9:
            ratings += 1 


        neighbors = G[current_node_coords]
        for neighbor in neighbors:
            if M[neighbor] == current_val + 1 and M[neighbor] <= 9:
                stack.append(neighbor)
    return ratings          

def solution1():
    total_score = 0
    for i in range(row):
        for j in range(col):
            if M[i,j] == 0:
                total_score += BFS_score(G, (i,j))
    return total_score

def solution2():
    total_ratings= 0
    for i in range(row):
        for j in range(col):
            if M[i,j] == 0:
                total_ratings += BFS_ratings(G, (i,j))
    return total_ratings