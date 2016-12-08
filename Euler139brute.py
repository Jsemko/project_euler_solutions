c=0

def get_gcd(m,n):
    if m*n ==0:return max(m,n)
    if n>m: return get_gcd(n,m)
    return get_gcd(n,m % n)

all_pairs = set()

for n in range(1,5000):
    if n % 100 ==0:print(n)
    for m in range(n+1, int((-n+(n**2 + 200000000)**.5)/2)+1,2):#range(n+1,int((5000**2-n**2)**.5),2):
        if get_gcd(m,n)==1:
            all_pairs.add((m,n))

tot = 0

for p in all_pairs:
    m,n = p
    if (m**2 + n**2) % (m**2 - n**2 - 2 *m*n)==0:
        print('Hit! with m = {m} and n = {n}'.format(m=m,n=n))
        perim = 2*m**2 + 2*m*n
        contrib = 100000000 // perim
        if 100000000 % perim ==0:
            contrib-=1
        print(contrib)
        tot +=contrib

print(len(all_pairs))
print(tot)