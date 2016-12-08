b = [0]*40
b[0] = 1
b[1] = 4

for i in range(2,40):
    b[i] = b[i-1] + b[i-2]

c = 1



for a in range(1,220000000):
    n = 5 * a**2 + 14*a +1
    if round((n**.5))**2 == n:
        print('ans = {a}, divisor is {d}'.format(a=a,d = a/b[c]))
        c+=1
