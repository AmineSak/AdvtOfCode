import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def get_input():
    with open("input.txt") as f:
        robots = []
        for line in f:
            robot = line.strip().split()
            p = list(map(int,robot[0][2:].split(",")))
            v = list(map(int,robot[1][2:].split(",")))
            robots.append([p,v])
        return robots
robots = get_input()

row = 103
col = 101

grid = np.zeros((row,col))
for r in robots:
    x,y = r[0]
    grid[y,x] += 1

def update_grid(times):
    for i in range(times):
        for r in robots:
                x1,y1 = r[0]
                vx, vy = r[1]
                x,y = (x1+vx)%col , (y1+vy)%row
                r[0] = [x,y]
                grid[y,x] += 1
                grid[y1,x1] -= 1
    return grid



def get_quadrants():
    quadrants = []
    row_mid = int((row + 1) / 2)
    col_mid = int((col + 1) / 2)

    # Divide the grid into quadrants
    quadrants = []
    quadrants.append(grid[:row_mid - 1, :col_mid - 1])          
    quadrants.append(grid[:row_mid - 1, col_mid :])     
    quadrants.append(grid[row_mid:, :col_mid - 1])     
    quadrants.append(grid[row_mid:, col_mid:])
    return quadrants

def solution1():
    ans = 1
    grid = update_grid(100)
    quadrants = get_quadrants()
    for q in quadrants:
        ans *= sum(sum(q))
    return ans

# solution 2
def save_as_bmp(filename):
    """Save the grid as a BMP image."""
    normalized_grid = (grid / grid.max() * 255).astype(np.uint8) if grid.max() > 0 else grid
    image = Image.fromarray(normalized_grid)
    image.save(filename, format="BMP")
    print(f"Grid saved as {filename}")

def solution2():
    mini = float("inf")
    seconds = 1
    for i in range(1):
        for r in robots:
            x1,y1 = r[0]
            vx, vy = r[1]
            x,y = (x1+vx)%col , (y1+vy)%row
            r[0] = [x,y]
            grid[y,x] += 1
            grid[y1,x1] -= 1
        quadrants = get_quadrants()
        s = 1
        for q in quadrants:
            s *= sum(sum(q))
        if mini > s:
            mini = s
            seconds = i + 1
    return seconds 

def show_tree():
    update_grid(6446)
    save_as_bmp("tree.bmp")
        
