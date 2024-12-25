

key_lock = open("input.txt").read().split("\n\n")

locks = []
keys = []

for kl in key_lock:
    kl = kl.splitlines()
    dum = []
    for line in kl:
        dum.append(list(line))
    dum1 = [0 for _ in range(len(dum[0]))]
    for j in range(len(dum[0])):
        for i in range(1,len(dum) - 1):
            if dum[i][j] == "#":
                dum1[j] += 1
        
    if dum[0][0] == "#":
        locks.append(dum1)
    else:
        keys.append(dum1)

def is_overlapping(k,l):
    pairs = list(zip(k,l))
    for pk,pl in pairs:
        if pk+pl > 5:
            return True
    return False
pairs = list()
for lock in locks:
    for key in keys:
        if not is_overlapping(key,lock):
            pairs.append((key,lock))
print(len(pairs))
        
