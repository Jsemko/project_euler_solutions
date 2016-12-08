def stair_rectangle(m,n,k):
    if m > n:return stair_rectangle(n,m,k)

    if k <= m: return (k +1 )* k //2

    if k <= n: return (m+1)*m //2 + m*(k-m)

    if k <= m+n -1: return (m+1)*m//2 + m*(k-m) - (k-n)*(k-n+1)//2

    return m*n

""" TESTING
print(stair_rectangle(4,8,2))
print(stair_rectangle(4,8,4))
print(stair_rectangle(4,8,6))
print(stair_rectangle(4,8,8))
print(stair_rectangle(4,8,10))
print(stair_rectangle(4,8,12))
print(stair_rectangle(4,8,14))
"""

m = 1; n = 10

ans = 10

def next_n(m,n):
    my_ans = 0
    for i in range(2,2*m,2):
        my_ans += stair_rectangle(i,2*m-i,2*n+1)
    for i in range(1,2*m,2):
        my_ans += stair_rectangle(i,2*m-i,2*n)
    return my_ans

all_cross = [[0]*48 for _ in range(48)]

all_cross[1][1] = 0

for n in range(2,48):
    all_cross[1][n] = all_cross[1][n-1] + next_n(1,n-1)
for m in range(2,48):
    all_cross[m][1] = all_cross[1][m]

for m in range(2,48):
    for n in range(2,48):
        all_cross[m][n] = all_cross[m][n-1] + next_n(m,n-1)

all_rect = [[0]*48 for _ in range(48)]

all_rect[1][1] = 1

for n in range(2,48):
    all_rect[1][n] = all_rect[1][n-1] + n
for m in range(2,48):
    all_rect[m][1] = all_rect[1][m]

for m in range(2,48):
    for n in range(2,48):
        all_rect[m][n]= all_rect[m][n-1] + n*(m+1)*m //2


All = 0
for i in range(1,48):
    for j in range(1,44):
        All += all_rect[i][j] + all_cross[i][j]

print(All)

