x,y = 1,1

def next_sol(x,y):
    for _ in range(2):
        x,y = 1*x + 2*y, y+x
    return x,y


while x < 2 * 10**12 - 1:
    x,y = next_sol(x,y)
print((y+1)/2)