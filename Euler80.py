def next_Nbc(a,b,c):
    N = int((a ** .5 + b) / c)
    return N, -b + c*N, int((a-(b-c*N)**2) / c)

def get_fundamental(N):
    last_h = 1
    h_0,b,c = next_Nbc(N,0,1)
    last_d = 0
    den = 1
    if c == 0: return 0
    for _ in range(1000):
        if c == 0: return 0
        next_num,b,c = next_Nbc(N,b,c)
        tmp = h_0
        h_0 = next_num*h_0 + last_h
        last_h = tmp
        tmp = den
        den = next_num*den + last_d
        last_d = tmp
    return h_0, den

total_sum = 0
for N in range(2,100):
    if N in [4,9,16,25,36,49,64,81]:continue
    s = 0
    num, den = get_fundamental(N)
    for _ in range(1000):
        digit = int(num/den)
        num = 10*(num - digit*den)
        s += digit
    print(N,s)
    total_sum +=s
print(total_sum)

