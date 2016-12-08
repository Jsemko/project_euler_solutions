def next_Nbc(a,b,c):
    N = int((a ** .5 + b) / c)
    return N, -b + c*N, int((a-(b-c*N)**2) / c)

def get_fundamental(N):
    last_h = 1
    h_0,b,c = next_Nbc(N,0,1)
    last_d = 0
    den = 1
    if c == 0: return 0
    while h_0 ** 2 != N * den **2 + 1:
        if c == 0: return 0
        next_num,b,c = next_Nbc(N,b,c)
        tmp = h_0
        h_0 = next_num*h_0 + last_h
        last_h = tmp
        tmp = den
        den = next_num*den + last_d
        last_d = tmp
    return h_0

m = 0
for N in range(1,1000):#range(1,10000):
    if m <get_fundamental(N):
        print(N)
        m = get_fundamental(N)

print(get_fundamental(997))