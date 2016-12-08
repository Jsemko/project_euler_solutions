

x = 993250; y = 949986; z = 856350
print(x+y+z)

def get_gcd(m,n):
    if m*n ==0:return max(m,n)
    if n>m: return get_gcd(n,m)
    return get_gcd(n,m % n)

all_pairs = []

for n in range(1,41):
    if n % 100 ==0:print(n)
    for m in range(n+1, 42):
        if get_gcd(m,n)==1:
            all_pairs.append((m,n))



all_pairs = [(m,n) for m,n in all_pairs if (m+n) % 2 ==1]

print(len(all_pairs))

def is_square(n):
    return round(n**.5)**2 == n

possible_c = sorted(all_pairs, key = lambda x:x[0]**2 + x[1]**2)

bound = 2799586

print(all_pairs)
count = 0



for m,n in possible_c:
    k = 1
    this_num = (k * (m**2 + n**2))**2
    while this_num <= bound:
        f = 2*k * m * n
        d = k * (m**2 - n**2)
        e = k * (m**2 + n**2)
        a = (f+2)
        z = (a**2 - f**2)//2
        while (3*z +this_num) <=  bound:
            if is_square(2*z + e**2):
                if is_square(2*z + f**2 + e**2):
                    print('hi ', 3*z + f**2 + e**2)
                    print("x = {x}, y = {y}, z = {z}".format(x = z + e**2, y = z + f**2, z = z))
                    print(m,n)
                    print(k)
            a+=2
            z = (a ** 2 - f ** 2) // 2
        k+=1
        this_num = (k * (m ** 2 + n ** 2)) ** 2

    k = 1
    this_num = (k * (m**2 + n**2))**2
    while this_num <= bound:
        d = 2*k* m * n
        f = k * (m**2 - n**2)
        e = k * (m**2 + n**2)
        a = (f+2)
        z = (a**2 - f**2)//2
        while 3*z +this_num <=  bound:
            if is_square(2*z + e**2):
                if is_square(2*z + f**2 + e**2):
                    print('hi ', 3*z + f**2 + e**2)
                    print("x = {x}, y = {y}, z = {z}".format(x = z + e**2, y = z + f**2, z = z))
                    #print(m,n)
            a+=2
            z = (a ** 2 - f ** 2) // 2
        k+=1
        this_num = (k  * (m ** 2 + n ** 2)) ** 2
    count+=1


