

def step(num):
    num = (num ^ (num * 64)) % 16777216
    num = ((num // 32) ^ num) % 16777216
    num = ((num*2048) ^ num) % 16777216
    return num

seq_total = {}
for line in open("input.txt").read().splitlines():
    num = int(line)
    seen = set()
    buyer = [num%10]
    for _ in range(2000):
        num = step(num)
        buyer.append(num%10)
    for i in range(len(buyer) - 4):
        a,b,c,d,e = buyer[i:i+5]
        seq = (b-a,c-b,d-c,e-d)
        if seq in seen: continue
        seen.add(seq)
        if seq not in seq_total: seq_total[seq] = 0
        seq_total[seq] += e
print(max(seq_total.values()))
        

        