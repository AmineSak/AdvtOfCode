import numpy as np
import re

def input_parser():
    # Open the file in read mode
    with open("input.txt", "r") as f:
        res = []  
        for line in f:
            line = np.array(list(line.strip()))  
            res.append(line)
        res = np.array(res)
    return res

s = input_parser()


def count_xmas(l):
    n = len(l)
    ans = 0
    for i in range(n):
        word = "".join(l[max(0,i):min(n , i + 4)])
        if word == "XMAS" or word == "SAMX":
            ans += 1
    return ans

def solution1(s):
    n = len(s)
    ans = 0
    # Sum occ on rows
    ans += sum([count_xmas(row) for row in s])

    # Sum occ on colums
    ans += sum([count_xmas(s[:,i]) for i in range(len(s))])

    # Sum occ on diagonals
    diags = [np.diag(s , k) for k in [-i for i in range(1,n)]+[i for i in range(n)]]
    anti_diags = [np.diag(np.fliplr(s) , k) for k in [-i for i in range(1,n)]+[i for i in range(n)]] 
    ans += sum([count_xmas(diag) for diag in diags] + [count_xmas(anti_diag) for anti_diag in anti_diags])

    return ans

def valid_X(X):
    diag = "".join(np.diag(np.fliplr(X)))
    anti_diag = "".join(np.diag(X))
    return (diag in {"MAS","SAM"} and anti_diag in {"MAS","SAM"})


def solution2(s):
    n = len(s)
    ans = 0
    for i in range(1,n-1):
        for j in range(1,n-1):
            if s[i,j] == "A":
                X = s[i-1:i+2 , j-1:j+2]
                ans += valid_X(X)
    return ans

solution2(s)
