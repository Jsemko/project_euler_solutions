import numpy as np

def ispal(n):
    return str(n) == str(n)[::-1]

arr = np.arange(1,7072)
squ = arr **2
csum = np.cumsum(squ)

print(csum[:5])

L = len(csum)
i = 0
subtract = 0
j =1
all_good = set()
current_sum = csum[j]-subtract
while i < L-1:
    while j < L and current_sum < 1e8:
        if ispal(current_sum):all_good.add(current_sum)
        current_sum = csum[j] - subtract
        j+=1
    subtract = csum[i]
    i+=1
    j=i+1
    if j >=L:break
    current_sum = csum[j]-subtract

all_good = [int(x) for x in all_good]

print(all_good)
print(sum(all_good))
