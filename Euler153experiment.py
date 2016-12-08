

def see_count(n):
    s = 0
    for i in range(1,n+1):
        s+= i*(n//i)
    return  s

for i in range(4,50):
    print('i = {i}, s = {s}'.format(i=i, s=see_count(i)))

print(see_count(10**8+1))