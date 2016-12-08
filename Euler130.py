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
primelist = primes_under(int(100000000000 ** .5) + 1)


def is_prime(n):
    if n ==1:return False
    if n ==2: return True
    top = n**.5 + 1
    l = len(primelist)
    i = 0
    cur_prime = primelist[i]
    while i < l and cur_prime <= top:
        if n % cur_prime == 0:
            return False
        i+=1
        cur_prime = primelist[i]
    return True

s=0
c=0

for i in range(91,1100000,2):
    if i % 5 == 0:continue
    if is_prime(i):continue
    d = 1
    n = 1
    while n % i != 0:
        d+=1
        n *=10
        n+=1
        n = n % i
    if (i-1) % d == 0:
        s+=i
        c+=1
    if c==25:
        break
print(s)