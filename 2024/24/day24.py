import re

def solve1():
    initialization, operations = open("input.txt").read().split("\n\n")
    
    initialization = initialization.strip().split("\n")
    operations = operations.strip().split("\n")
    operations = [tuple(op.split()) for op in operations]
    
    xy ={}
    for line in initialization:
        key, val = line.split(":")
        xy[key] = int(val)

    while True:
        if not operations:
            break
        for op in operations:
            a,x,b,_,c = op
            if a in xy and b in xy:
                if x == "AND":
                    xy[c] = (xy[a] & xy[b])
                elif x == "OR":
                    xy[c] = (xy[a] | xy[b])
                elif x == "XOR":
                    xy[c] = (xy[a] ^ xy[b])
                operations.remove(op)

    z = {k:v for k,v in xy.items() if "z" in k}
    keys = list(z.keys())
    keys.sort(reverse=True)
    return int("".join([str(z[k]) for k in keys]),2)

print("Solution for part I: ",solve1())

def solve2():
    with open("input.txt") as f:
        data = f.read().split("\n\n")

    xs, ys = {}, {}

    for l in data[0].splitlines():
        d = xs if "x" in l else ys
        ps = l.split(":")
        d[ps[0]] = int(ps[1])

    ops = {}
    rev_ops = {}

    for l in data[1].splitlines():
        ps = l.split()
        assert ps[4] not in ops
        ops[ps[4]] = (ps[0], ps[1], ps[2])

        rev_ops[(ps[0], ps[1], ps[2])] = ps[4]
        rev_ops[(ps[2], ps[1], ps[0])] = ps[4]

    top = max({int(d[1:]) for d in ops if re.match(r"z\d+", d)})

    wrong_gates = set()

    for i in range(1, top):
        x = f"x{i:02d}"
        y = f"y{i:02d}"
        z = f"z{i:02d}"

        res_op = ops[z]

        xor_gate = rev_ops[(x, "XOR", y)]
        and_gate = rev_ops[(x, "AND", y)]

        if "XOR" not in res_op:
            wrong_gates.add(z)

        carry = [set(o).difference({"XOR", xor_gate})
                 for o in ops.values() if "XOR" in o and xor_gate in o]
        if len(carry) != 1:
            wrong_gates.add(xor_gate)
            wrong_gates.add(and_gate)
        else:
            carry = carry[0].pop()
            xor2_gate = rev_ops[(xor_gate, "XOR", carry)]
            if xor2_gate != z:
                wrong_gates.add(xor2_gate)

    print(",".join(sorted(list(wrong_gates))))
solve2()
        