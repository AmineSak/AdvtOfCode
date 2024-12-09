from collections import defaultdict
from itertools import batched

def get_input():
    with open("input.txt") as f:
        line = f.readline()
        res = list(map(int, line))
    return res

raw = get_input()
disk = []
files = defaultdict(int)
for i in range(len(raw)):
    if i % 2 == 0:
        disk += [i//2 for _ in range(raw[i])]
        files[i//2] = raw[i]
    else:
        disk += [None for _ in range(raw[i])]
    
l = 0
r = len(disk) - 1

def solution1(disk):
    l = 0
    r = len(disk) - 1
    check_sum = 0
    while l < r:
        if disk[r] != None and disk[l] == None:
            disk[r] , disk[l] = disk[l], disk[r]
            l += 1
            r -= 1
        elif disk[r] != None and disk[l] != None:
            l += 1
        elif disk[l] == None:
            r -= 1
        else:
            l += 1
            r -= 1
    for i in range(len(disk)):
        if disk[i] != None:
            check_sum += i * disk[i]
    
    return  check_sum

def solution2(layout):
    data_blocks = []
    free_blocks = []
    file_id = 0
    # Create parallel lists representing chunks
    # of data, and the free space following it
    for b in batched(layout, 2):
        data_size, *rest = b
        empty_size = rest[0] if len(rest) == 1 else 0

        data_blocks.append([file_id] * data_size)
        free_blocks.append([[], empty_size])
        file_id += 1

    # Defragment
    candidate_id = len(data_blocks)
    while candidate_id > 1:
        candidate_id -= 1
        candidate_data = data_blocks[candidate_id]
        candidate_len = len(candidate_data)

        # Find a free block with enough space for current candidate
        for i in range(candidate_id):
            # Skip if this free block is too small to hold the candidate data
            if free_blocks[i][1] < candidate_len:
                continue

            # Move candidate data into the free block, and update its size
            free_blocks[i][0].extend(candidate_data)
            free_blocks[i][1] -= candidate_len

            # Null the original data block
            data_blocks[candidate_id] = [None] * candidate_len
            break

    # Calculate checksum
    s, pos = 0, 0
    for i in range(len(data_blocks)):
        for d in data_blocks[i]:
            s += (d or 0) * pos
            pos += 1
        for d in free_blocks[i][0]:
            s += d * pos
            pos += 1
        pos += free_blocks[i][1]

    return s