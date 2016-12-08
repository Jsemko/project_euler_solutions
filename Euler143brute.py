fin = '/Users/jeremy/pair_squares.txt'

fio = open(fin)

pair_dict = dict()

while 1:
    l = fio.readline()
    if not l:break
    a,b = l.split()
    a = int(a)
    b = int(b)
    if a in pair_dict:
        pair_dict[a].append(b)
    else:
        pair_dict[a]=[b]

keys = sorted(list(pair_dict.keys()))

import itertools

allcombos = set()


for k in keys:
    if len(pair_dict[k]) > 1:
        for c1,c2 in itertools.combinations(pair_dict[k],2):
            if c1 in pair_dict.keys():
                if c2 in pair_dict[c1]:
                    if k + c1 + c2 <= 120000:
                        print('hit! We have p+q+r = {ans}'.format(ans = k + c1 + c2))
                        allcombos.add(k+c1+c2)

print(sum(allcombos))


