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
primelist = primes_under(int(1000000) + 1)


p = primelist[0]
i = 1

while 2*p*i < 1e10:
    i+=2
    p=primelist[i-1]
    print(p)
print(i)