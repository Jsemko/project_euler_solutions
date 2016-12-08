fin = '/Users/Jeremy/Desktop/p107_network.txt'

test = """-	16	12	21	-	-	-
16	-	-	17	20	-	-
12	-	-	28	-	31	-
21	17	28	-	18	19	23
-	20	-	18	-	-	11
-	-	31	19	-	-	27
-	-	-	23	11	27	-"""
test = test.replace('\t',',').split('\n')
test = [c.replace('-','0') for c in test]
test = [[int(c) for c in l.split(',')] for l in test]
print(test)

import numpy as np

def is_connected(con):
    return np.max( np.min(np.linalg.matrix_power(con,len(con[:,0])) + np.linalg.matrix_power(con,1+ len(con[:,0]))) )


io = open(fin)

adj = []

while True:
    l = io.readline()
    if not l: break
    l = l.replace('-','0').split(',')
    adj.append([int(c) for c in l])


#adj = test
adj = np.array(adj)

con = adj > 0

to_remove = []

m, n = con.shape

for i in range(m-1):
    for j in range(i+1,m):
        if con[i,j]:
            to_remove.append((i,j,adj[i,j]))

to_remove = sorted(to_remove,key = lambda x:-x[2])

print(to_remove)

weight_removed = 0

for c in to_remove:
    next_con = con.copy()
    next_con[c[0],c[1]] = 0
    next_con[c[1],c[0]] = 0
    if is_connected(next_con):
        con = next_con
        weight_removed += adj[c[0],c[1]]
        print(adj[c[0],c[1]])

print(sum(np.linalg.matrix_power(con,40)))

print(sum(con))

print(weight_removed)
print(np.sum(adj)/2)

print(np.sum(adj)/2 - weight_removed)
