
C = dict()

C[3] = [[0]* 10 for _ in range(10)]

import itertools

for i,j in itertools.product(range(10),repeat=2):
    C[3][i][j] = max(0, 10 - i - j)

print(C[3][3][3])

for d in range(4,21):
    C[d] = [[0]* 10 for _ in range(10)]
    for i,j,k in itertools.product(range(10),repeat=3):
        if i+j+k <= 9:
            C[d][i][j] += C[d-1][j][k]

s= 0

for i in range(1,10):
    for j in range(10):
        s+=C[d][i][j]

print(s)
