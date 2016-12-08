def n_cubes(a,b,c,l):
    base = 2*(a*b+a*c+b*c)
    edge = 4*(a+b+c)
    return base + edge*(l-1) + 4*(l-1)*(l-2)

all_C = []

lim = 20000

a = 1
a_lim = round((lim /6)**.5)
for a in range(1,a_lim+1):
    b_lim = round((lim/2)**.5)
    for b in range(a,b_lim+1):
        for c in range(b,round(lim/4)+1):
            l = 1
            n = n_cubes(a,b,c,l)
            while n <= lim:
                all_C.append(n)
                l+=1
                n = n_cubes(a,b,c,l)

from collections import Counter

c = Counter(all_C)
print([(k,v) for k,v in c.items() if v == 1000])