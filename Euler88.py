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

primelist = primes_under(int(24000 ** .5) + 1)



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

def next_set(c_set,n):
    n_set = []
    for l in c_set:
        add_list = l.copy()
        add_list.append(n)
        add_list.sort()
        n_set.append(add_list)
        for i in range(len(l)):
            mult_list = l.copy()
            mult_list[i] *= n
            mult_list.sort()
            n_set.append(mult_list)
    output = []
    for l in n_set:
        if not l in output:
            output.append(l)
    return output



def get_possibilities(l,number):
    if len(l) == 1:return None
    current_set = [[l.pop()]]
    for n in l:
        current_set = next_set(current_set,n)
    possibilities = set()
    for l in current_set:
        length = len(l)
        if length == 1: continue
        remaining = number - sum(l)
        possibilities.add(remaining + length)
    return possibilities

first_time = [0]*24001

for i in range(4,24000):
    s = get_possibilities(prime_factor(i),i)
    if s:
        for n in s:
            if first_time[n] == 0:
                first_time[n] = i

print(sum(set(first_time[:12001])))
