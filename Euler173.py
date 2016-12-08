Lim = 10 ** 6

count =0
for n in range(3,Lim//4 + 2):
    for k in range(n-2,0,-2):
        if n**2-k**2 > Lim:break
        count+=1

print(count)