import numpy as np

def get_int_matrix(filename):
    with open (filename, 'r') as f:
        res = []
        for line in f:
            row = np.array(list(map(int,list(line.strip()))))
            res.append(row)
        res = np.array(res)
    return res

def get_char_matrix(filename):
    with open (filename, 'r') as f:
        res = []
        for line in f:
            row = np.array(list(line.strip()))
            res.append(row)
        res = np.array(res)
    return res