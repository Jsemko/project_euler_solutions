Lim = 10 ** 6

count =0

unique_values = dict()

for n in range(3,Lim//4 + 2):
    for k in range(n-2,0,-2):
        value = n**2-k**2
        if value > Lim:break
        if value in unique_values:
            unique_values[value] +=1
        else:
            unique_values[value] = 1
        count+=1

test = 0
for v in unique_values:
    if unique_values[v] <= 10:
        test+=1
print(test)
