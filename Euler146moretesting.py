ans = [10,315410, 927070,2525870,8146100]


import random

def prob_prime(n):
    s = 0
    d = n -1
    while d % 2 ==0:
        s+=1
        d //= 2


    def this_test(a):
        if pow(a,d,n) == 1:
            return False
        for i in range(s):
            if pow(a,2**i *d,n) == n-1:
                return False
        return True

    for i in range(5):
        a = random.randrange(2,n)
        if this_test(a):
            return False

    return True

for n in range(8146110,150000000,10):
    if n % 1000000 == 0:
        print(n)
    N = n**2
    for j in range(1,28,2):
        if j in [1,3,7,9,13,27]:
            if not prob_prime(N+j):
                break
        else:
            if prob_prime(N+j):
                break
    else:
        print("hit! Is {n}".format(n=n))
        ans.append(n)


print(sum(ans))
