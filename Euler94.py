def ans(x):
    return (2*x + 1)/3

def ans2(x):
    return (2*x - 1)/3

def next_one(x,y):
    x,y = 2*x + 3*y, 2*y + x
    return x,y

x,y = 2,1

tot = 0

lim = 333333333 #333333334

x,y = next_one(x,y)
value = ans(x)
print(value)
parity = 0
while value < lim:
    x,y = next_one(x,y)
    if parity % 2 == 0:
        tot += 3*value+1
        value = ans2(x)
        print(value)
    else:
        tot += 3*value -1
        value = ans(x)
        print(value)
    parity +=1
print(tot)