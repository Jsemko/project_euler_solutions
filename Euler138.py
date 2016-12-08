# find solutions to x**2 - 5 * n**2 = pm 1

x_0,n_0 = 2,1

n_L = 12

def next_ans(x,y):
    return x_0 * x + 5*n_0*y, x_0*y+n_0*x

T= 0
x,n = x_0,n_0
for i in range(n_L):
    A = (x + 2 * n) * 2 * n
    L = int(((2*A+(-1)**(i+1))**2 + (A**2))**.5)
    print(L)
    T+=L
    x,n = next_ans(x,n)
print(T)
