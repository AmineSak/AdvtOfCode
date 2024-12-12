import numpy as np

def get_char_matrix(filename):
    with open (filename, 'r') as f:
        res = []
        for line in f:
            row = np.array(list(line.strip()))
            res.append(row)
        res = np.array(res)
    return res

M = get_char_matrix("test.txt")

def in_blob(point, char):
    i, j = point
    return (0<=i<len(M) and 0<=j<len(M[0])) and M[i,j] == char

def get_neighbors(point):
    i,j = point
    neighbors = [(i-1, j), (i+1 , j), (i, j+1),(i, j-1)] 
    neighbors = [(i,j) for (i,j) in neighbors if 0<=i<len(M) and 0<=j<len(M[0])]
    return neighbors

def get_edges(point):
    neighbors = get_neighbors(point)
    edges = 0
    if len(neighbors) == 3:
        edges = 1
    elif len(neighbors) == 2:
        edges = 2
    for n in neighbors:
        if M[n] != M[point]:
            edges += 1
    return edges

def get_corners(point, char):
    dirs = [(-1,0), (0,1), (1,0), (0,-1)]
    i, j = point
    corners = 0
    for k in range(4):
        dir1 = dirs[k]
        dir2 = dirs[(k+1) % 4]
        if (not in_blob((i+dir1[0],j+dir1[1]),char)) and (not in_blob((i+dir2[0],j+dir2[1]),char)):
            corners += 1
        elif in_blob((i+dir1[0],j+dir1[1]),char) and in_blob((i+dir2[0],j+dir2[1]),char) and (not in_blob((i+dir2[0]+dir1[0],j+dir2[1]+dir1[1]),char)):
            corners += 1

    return corners
        
    

def DFS(point,char,blob_props,visited):
    # Continue if the current point is valid (i.e not visited and have the same label (same character))
    if M[point] != char or point in visited :
        return
    
    visited.add(point)
    # Add the contribution of the current node to the area of the current blob
    blob_props[0] += 1
    # Add the contribution of the current node to the total perimeter of the current blob (i.e count the number of the edges based on its neighbors)
    blob_props[1] += get_edges(point)

    neighbors = get_neighbors(point)

    for neighbor in neighbors:
        DFS(neighbor,char,blob_props,visited)

def DFS_corners(point,char,blob_props,visited):
    # Continue if the current point is valid (i.e not visited and have the same label (same character))
    if M[point] != char or point in visited :
        return
    
    visited.add(point)
    # Add the contribution of the current node to the area of the current blob
    blob_props[0] += 1
    # Add the contribution of the current node to the total sides count
    blob_props[1] += get_corners(point, char)

    neighbors = get_neighbors(point)

    for neighbor in neighbors:
        DFS(neighbor,char,blob_props,visited)

def soluion1():
    visited = set()
    total_fencing_cost = 0
    # Traverse the Matrix and for each point initiate a Blob detction (DFS)
    for i in range(len(M)):
        for j in range(len(M[1])):
            char = M[i,j]
            current_blob_area = 0
            current_blob_per = 0
            blob_props = [current_blob_area, current_blob_per]
            DFS((i,j),char,blob_props,visited)
            # after the DFS is done calculate the fence cost of the blob
            total_fencing_cost += blob_props[0]* blob_props[1]

    return total_fencing_cost
    
 
def soluion2():
    visited = set()
    total_fencing_cost = 0
    # Traverse the Matrix and for each point initiate a Blob detction (DFS)
    for i in range(len(M)):
        for j in range(len(M[1])):
            char = M[i,j]
            current_blob_area = 0
            current_blob_cor = 0
            blob_props = [current_blob_area, current_blob_cor]
            DFS_corners((i,j),char,blob_props,visited)
            # after the DFS is done calculate the fence cost of the blob
            total_fencing_cost += blob_props[0]* blob_props[1]

    return total_fencing_cost


