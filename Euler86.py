def gen_triples(M):
    all_guys = set()
    for n in range(1,M):
        for m in range(n+1,M //(2*n)+1):
            a = m**2 - n**2
            b = 2*m*n
            if a > M or b > M:continue
            if a > b:
                tmp = a
                a = b
                b = tmp
            for k in range(1, (M // b) + 1):
                all_guys.add((a*k,b*k))
    return  all_guys



M = 1818
s= 0
last = 0
for i in gen_triples(2* M):
    if i[0] > M:continue
    if i[1] <= M:
        s += ((i[0]) // 2)
    s += max((i[1] // 2) - (i[1] - i[0] - 1), 0)
    last = s

print(s)

