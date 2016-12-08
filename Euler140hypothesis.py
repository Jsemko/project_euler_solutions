b = [0]*100
b[0] = 1
b[1] = 4

a = [0]*100
a[0] = 1
a[1] = 1

for i in range(2,100):
    b[i] = b[i-1] + b[i-2]
    a[i] = a[i-1] + a[i-2]
s= 0
for i in range(1,31,2):
    ans = a[i]*b[i+1]
    print(ans-a[i*2+1])
    print(ans)
    s+=ans*2 -a[i*2+1]

print(s)