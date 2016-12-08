def primes_under(m):
    primes = [2]
    for i in range(3,m,2):
        if (i + 1)% 100000 == 0: print('done ' + str(i))
        j = 0
        while j < len(primes) and i >= primes[j]**2:
            if i % primes[j] == 0: break
            j+=1
        else: primes.append(i)
    return primes
primelist = primes_under(int(120000 ** .5) + 1)

print(primelist[-1])


def prime_factor(n):
    l = len(primelist)
    i = 0
    factor = []
    while n > 1 and i < l:
        if n % primelist[i] == 0:
            n //= primelist[i]
            factor.append(primelist[i])
        else:
            i+=1
    if factor:
        if n > 1:factor.append(n)
        return factor
    else: return [n]


def rad(n):
    f = prime_factor(n)
    f = set(f)
    ans = 1
    for p in f:
        ans *= p
    return ans

rad_d = dict()
pf_d = dict()
for i in range(1,120001):
    pf_d[i] = set(prime_factor(i))
    rad_d[i] = rad(i)

possible_c = []

for i in range(1, 120000):
    if rad_d[i] < i: possible_c.append(i)

print(len(possible_c))

c_hits = []
counter = 0
for c in possible_c:
    if counter % 1000 ==0:print('done {steps}'.format(steps = counter))
    for a in range(1,c//2):
        b= c-a
        if pf_d[a].intersection(pf_d[b]):
            continue
        if pf_d[a].intersection(pf_d[c]):
            continue
        if pf_d[b].intersection(pf_d[c]):
            continue
        if rad_d[a]*rad_d[b]*rad_d[c] < c:
            c_hits.append(c)
    counter +=1

print(sum(c_hits))