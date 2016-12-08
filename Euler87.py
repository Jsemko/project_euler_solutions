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
primelist = primes_under(int(50000000 ** .5) + 1)

print(len(primelist))

specials = set()

for p1 in primelist:
    for p2 in primelist:
        for p3 in primelist:
            cand = p1**2 + p2 **3 + p3 **4
            if cand < 50000000: specials.add(cand)
            else: break

print(len(specials))
