from functools import cache
from collections import defaultdict

lines = open("input.txt").read().splitlines()

patterns = set(lines[0].split(", "))
maxlen = max(list(map(len, patterns)))

@cache
def solve1(design):
    if design == "": return True
    for i in range(min(maxlen, len(design)) + 1):
        if design[:i] in patterns and solve1(design[i:]):
            return True
    return False

# Without @cache
Cache = defaultdict(int)
def solve1_(design):
    if design == "": return True
    if design in Cache: return Cache[design] 
    for i in range(min(maxlen, len(design)) + 1):
        if design[:i]  in patterns and solve1_(design[i:]):
            Cache[design] = True  
            return True
    Cache[design] = False
    return False

Counter = defaultdict(int)
def solve2(design):
    if design == "": return 1
    if design in Counter : return Counter[design]
    for i in range(min(maxlen,len(design)) + 1):
        if design[:i] in patterns:
            Counter[design] += solve2(design[i:])
    return Counter[design]
print("Solution 1 :", sum([solve1_(design) for design in lines[2:]]))
print("Solution 2 :", sum([solve2(design) for design in lines[2:]]))