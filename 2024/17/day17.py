
def get_input(filename):
    reg = {"A":0, "B": 0, "C":0}
    p1, p2 = open(filename).read().split("\n\n")
    a,b,c = p1.strip().split("\n")
    a,b,c = a.split()[2], b.split()[2], c.split()[2]
    reg["A"] = int(a)
    reg["B"] = int(b)
    reg["C"] = int(c)
    prog = list(map(int,p2.split()[1].split(",")))
    return reg,prog

reg, prog = get_input("input.txt")

# prog: intruction, combo operand encoding , instruction, combo operand encoding ,...., ....
combo = {0:0,1:1,2:2,3:3,4:"A",5:"B",6:"C"}
def adv(operand):
    operand = combo[operand] if type(combo[operand]) == int else reg[combo[operand]]
    numerator = reg["A"]
    denominator = 2**operand
    reg["A"] = numerator // denominator
def bxl(operand):
    reg["B"] = reg["B"] ^ operand
def bst(operand):
    operand = combo[operand] if type(combo[operand]) == int else reg[combo[operand]]
    reg["B"] = operand % 8
def jnz():
    # points to the literal value of the operand
    if reg["A"] != 0:
        return True
    return False
def bxc():
    reg["B"] = reg["B"] ^ reg["C"]
def bdv(operand):
    operand = combo[operand] if type(combo[operand]) == int else reg[combo[operand]]
    numerator = reg["A"]
    denominator = 2**operand
    reg["B"] = numerator // denominator
def cdv(operand):
    operand = combo[operand] if type(combo[operand]) == int else reg[combo[operand]]
    numerator = reg["A"]
    denominator = 2**operand
    reg["C"] = numerator // denominator

def solve1():
    ip = 0
    output = ""
    while ip < len(prog) - 1:
        ins, op = prog[ip], prog[ip+1]
        if ins == 0:
            adv(op)
        if ins == 1:
            bxl(op)
        if ins == 2:
            bst(op)
        if ins == 3:
            if jnz():
                ip = op
                continue
        if ins == 4:
            bxc()
        if ins == 5:
            op = combo[op] if type(combo[op]) == int else reg[combo[op]]
            if output == "":
                output = f"{op%8}"
            else:
                output += f",{op%8}"
        if ins == 6:
            bdv(op)
        if ins == 7:
            cdv(op)
        ip += 2
    
    return output


# b = a % 8
# b = b ^ 5
# c = a >> b
# b = b ^ 6
# a = a >> 3
# b = b ^ C
# out(b % 8) 
# jnz a to 7

def solve2(program,ans):
    print(prog,ans)
    if program == [] :return ans
    for t in range(8):
        a = ans << 3 | t
        b = a % 8
        b = b ^ 5
        c = a >> b
        b = b ^ 6
        b = b ^ c
        if b % 8 == program[-1]:
            sub = solve2(program[:-1],a)
            if sub is None: continue
            return sub
print('sol1: ',solve1(),"\nsol2: ",solve2(prog,0))

