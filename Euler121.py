import numpy as np

def get_prob(turns):
    winning_discs = turns // 2 + 1
    arr = np.zeros((winning_discs+1,turns+1),dtype=np.float64)
    arr[0,:]=1
    for j in range(1,turns+1):
        for i in range(1,winning_discs +1):
            arr[i,j] = (1/(2 + turns - j)) * arr[i-1,j-1] + ((1+turns -j )/(2+turns - j) * arr[i,j-1])
    print(arr)
    print(arr[-1,-1])
    return arr[-1,-1]

a = get_prob(15)

print(int(1/a))