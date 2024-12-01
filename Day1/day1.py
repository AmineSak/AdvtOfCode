from collections import Counter
def input_to_lists():
    f = open("input.txt","r")
    l1 = []
    l2 = []
    for line in f:
        num1 , num2 = line.split()
        l1.append(int(num1))
        l2.append(int(num2))
    return l1, l2

l1 , l2 = input_to_lists()

def calc_sum(l1 , l2):
    l1.sort()
    l2.sort()
    n = len(l1)
    sum = 0
    for i in range(n):
        sum += abs(l1[i] - l2[i])
    return sum

# print(calc_sum(l1,l2))

def similarity_score(l1,l2):
    counter = Counter(l2)
    n = len(l1)
    score = 0
    for i in range(n):
        if l1[i] in counter:
            score += l1[i] * counter[l1[i]]
    
    return score

print(similarity_score(l1, l2))
