def check_increasing(my_list):
    for i in range(2,1+(len(my_list) + 1)//2):
        if sum(my_list[:i]) <= sum(my_list[-1:-i:-1]):return False
    return True

fin = '/Users/Jeremy/Desktop/p105_sets.txt'

io = open(fin)
import itertools


s = 0
ctr = 0
while True:
    l = io.readline()
    if not l: break
    my_set = sorted([int(c) for c in l.split(',')])
    if not check_increasing(my_set): continue
    all_sums = []
    for r in range(1,1+len(my_set)):
        for c in itertools.combinations(my_set,r):
            all_sums.append(sum(c))
    if len(all_sums) > len(set(all_sums)): continue
    print(my_set)
    ctr +=1
    s += sum(my_set)

print(ctr,s)

