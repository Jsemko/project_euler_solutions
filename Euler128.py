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

print(primelist[-1])


def is_prime(n):
    if n ==1:return False
    if n ==2: return True
    top = n**.5 + 2
    l = len(primelist)
    i = 0
    cur_prime = primelist[i]
    while i < l and cur_prime <= top:
        if n % cur_prime == 0:
            return False
        i+=1
        cur_prime = primelist[i]
    return True

ans = [1,2]

current = 8
last_increment = 6

while len(ans) < 2000:
    increment = last_increment + 6
    next_increment = increment + 6
    print(last_increment,increment,next_increment)
    if is_prime(increment-1) and is_prime(increment+1) and is_prime(increment + next_increment-1):
        ans.append(current)
    if is_prime(increment-1) and is_prime(last_increment+increment-1) and is_prime(next_increment -1):
        ans.append(current+increment-1)
    current +=increment
    last_increment = increment

print(ans[1999])
