import re
def input_parser():
    f = open("input.txt","r")
    res = ""
    for line in f:
        res += line
    return res

s = input_parser()


def extract_multiplications(s):
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    return re.findall(pattern , s)

def calculate_operation(segment):
    num1 , num2 = segment[4:-1].split(",")
    return int(num1) * int(num2)


def calculate_operations(s):
    operations = extract_multiplications(s)
    res = 0
    for op in operations:
        res += calculate_operation(op)
    return res



def calculate_operations_cond(s):
    pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
    matches = re.findall(pattern, s)
    ans = 0
    flag = True
    for match in matches:
        if match == "do()":
            flag = True
        elif match == "don't()":
            flag = False
        else:
            if flag: 
                ans += calculate_operation(match)

    return ans

# Puzzle 1
print(calculate_operations(s))

#Puzzle 2
print(calculate_operations_cond(s))
