

x,y,z = 929209201, 885636000, 788810400
print(x+y+z)

def get_gcd(m,n):
    if m*n ==0:return max(m,n)
    if n>m: return get_gcd(n,m)
    return get_gcd(n,m % n)

c_to_pairs = dict()

for n in range(1,225):
    if n % 100 ==0:print(n)
    for m in range(n+1, 226):
        if get_gcd(m,n)==1:
            c = 2*m*n
            if c in c_to_pairs:
                c_to_pairs[c].append((m,n))
            else:
                c_to_pairs[c] = [(m,n)]

print(len(c_to_pairs))

def is_square(n):
    return round(n**.5)**2 == n

possible_c = sorted(c_to_pairs.keys())

import itertools

top = 10**30

for c in possible_c:
    if len(c_to_pairs[c]) > 1:
        for l,r in itertools.combinations(c_to_pairs[c],2):
            if is_square(abs((l[0]**2 - l[1]**2)**2 - (r[0]**2 - r[1]**2)**2)):
                e = max(r[0] ** 2 - r[1] ** 2,(l[0]**2 - l[1]**2) )
                d = min(r[0] ** 2 - r[1] ** 2,(l[0]**2 - l[1]**2) )
                a = round((e**2 + c**2)**.5)
                b = round((d**2 + c**2)**.5)
                f = round((a**2 - b**2)**.5)
                if  a**2 + d**2 > c**2 + f**2 and c**2 + f**2 > b**2 - e**2 and b**2 - e**2 > 0:
                    print(
                        "c = {c}, d = {d}, e = {e}, a = {a}, b = {b}, f = {f}".format(
                            c = c,
                            d = d,
                            e = e,
                            a = a,
                            b = b,
                            f = f
                        )
                    )
                    x = (a ** 2 + d ** 2 + c ** 2 + f ** 2 + b ** 2 - e ** 2) // 2
                    print("answer is = {x}".format(x = x))
                    if x < top:
                        top = x
                        print('Best is ' +str(x))

print('best I got was ' + str(top))