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
primelist = primes_under(int(200000 ** .5) + 1)

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
        ans*=p
    return ans


my_list = list(range(1,100001))


a= sorted(my_list,key=lambda x:(rad(x),x))
print(a)
print(a[9999])