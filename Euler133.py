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
primelist = primes_under(int(100000) + 1)

print(sum(primelist) - 748832)

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

ans = []

for i in primelist:
    if i <10:continue
    if i % 5 == 0: continue
    d = 2
    n = (10 ** d - 1) // 9
    while n % i != 0:
        d += 1
        n *= 10
        n += 1
        n = n % i
    if not set(prime_factor(d)).difference({2,5}):
        print(i)
        ans.append(i)

print(ans)
print(sum(ans))
sum(primelist) -sum(ans)