
def get_input():
    with open("input.txt") as f:
        line = f.readline()
        return list(map(int,list(line.strip().split())))

l = get_input()

def r1(n):
    return [1]

def r2(n):
    num = n
    leng = len(str(num))
    num_s = str(num)
    return [int(num_s[:leng//2]),int(num_s[leng//2:])]

def r3(n):
    return [n * 2024]

rules_cache = {}
def rules(n):
    if n in rules_cache:
        return rules_cache[n]
    elif n == 0:
        result = r1(n)
    elif len(str(n)) % 2 == 0:
        result = r2(n)
    else:
        result = r3(n)
    rules_cache[n] = result
    return result

def solution(blinks):
    count = {}
    
    for rock in l:
        count[rock] = 1
    
    for b in range(blinks):
        next_count = {}
        for rock, size in count.items():
            for res in rules(rock):
                next_count[res] = next_count.get(res,0) + size
        count = next_count

    return sum(count.values())   
memo = {}
