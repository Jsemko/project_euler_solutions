def next_Nbc(a,b,c):
    N = int((a ** .5 + b) / c)
    return N, -b + c*N, int((a-(b-c*N)**2) / c)

def cycle_length(N):
    pairs_seen = []
    pairs_seen.append((0,1))
    _,b,c = next_Nbc(N,0,1)
    if c == 0: return 0
    while (b,c) not in pairs_seen:
        if c == 0: return 0
        pairs_seen.append((b,c))
        _,b,c = next_Nbc(N,b,c)
    return len(pairs_seen) - pairs_seen.index((b,c))

s = 0
for N in range(1,10000):
    if cycle_length(N) % 2 == 1:s+=1
print(s)
