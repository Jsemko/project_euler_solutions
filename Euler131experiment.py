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
primelist = primes_under(int(10000000**.5) + 1)



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

if 0:
    for n in range(1,10000):
        for a in range(1,int((n**2 * (n+1e6))**(1/3))):
            rhs = a*(3*n**2+3*a*n+a**2)
            if rhs % n**2 ==0:
                rhs //= n**2
                if is_prime(rhs):
                    print('p = {rhs}, n = {n}, and a = {a}'.format(rhs=rhs,n=n,a=a))


s=0
for l in range(578):
    p = 3*l**2 + 3*l +  1
    if p > 1e6:break
    if is_prime(p):
        print('p = {rhs}, n = {n}, and a = {a}'.format(rhs=p, n= l**3, a=l**2))
        s+=1

print(s)


