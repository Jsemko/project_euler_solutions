

primes_excluded = [11,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73]

others_excluded = [22,33,44,55,66,77]
others_excluded.extend([34,51,68])
others_excluded.extend([38,57,76])
others_excluded.extend([46,69])
others_excluded.extend([58])
others_excluded.extend([62])
others_excluded.extend([74])

remaining_primes = [2,3,5,7,13]

all_excluded = set(primes_excluded).union(set(others_excluded))

candidates = [n for n in range(3,81) if not n in all_excluded]

print(candidates)
P = 1

for c in candidates:
    P *= c**2

LHS = P // 4

big_candidates = {c:P//c**2 for c in candidates}

"""
print(LHS)
for b in big_candidates:
    print(b)
"""

def count_factors(n):
    the_num = P
    count = 0
    while the_num % n == 0:
        the_num //= n
        count+=1
    return count

"""
test_list = [3,4,5,7,12,15,20,28,35]
test_sum = sum([big_candidates[n] for n in test_list])
"""

import itertools
def get_combos(n):
    power = count_factors(n)
    divisor = n ** power
    remainders = [big_candidates[i] % divisor for i in candidates if i % n == 0]
    local_candidates = [i for i in candidates if i % n == 0]
    total_count = 0
    count = 0
    all_combos = []
    for combos in itertools.product([0,1],repeat=len(remainders)):
        total_count+=1
        if total_count % 1000000 == 0:print('total is {t}, count is {c}'.format(t=total_count,c=count))
        current_sum = sum([remainders[i] for i in range(len(remainders)) if combos[i] ==1 ])
        if current_sum % divisor == 0:
            count +=1
            all_combos.append([local_candidates[i] for i in range(len(remainders)) if combos[i] ==1 ])
    print(len(all_combos))
    return all_combos

print(get_combos(13))

all_combos= dict()
all_combos[3] = get_combos(3)
all_combos[5] = get_combos(5)
all_combos[7] = get_combos(7)
all_combos[13] = get_combos(13)

def is_valid(n,m,list1,list2):
    l1 = set(list1)
    l2 = set(list2)
    for k in list1:
        if k % m == 0:
            if not k in l2:
                return False
    for k in list2:
        if k % n == 0:
            if not k in l1:
                return False
    return True

count = 0
hit = 0
total_hits = 0
powers_of_2 = [4,8,16,32,64]

for l3,l5,l7,l13 in itertools.product(all_combos[3],all_combos[5],all_combos[7],all_combos[13]):
    count +=1
    if count % 2000000 == 0: print('count is {c}, hits are {h},total hits are {t}'.format(c= count,h=hit, t = total_hits))
    if not is_valid(3,5,l3,l5):continue
    if not is_valid(3,7,l3,l7):continue
    if not is_valid(3,13,l3,l13):continue
    if not is_valid(5,7,l5,l7):continue
    if not is_valid(5,13,l5,l13):continue
    if not is_valid(7,13,l7,l13):continue
    all_items = sorted(list(set(l3).union(set(l5)).union(set(l7)).union(set(l13))))
    hit +=1
    remainder = LHS - sum([big_candidates[i] for i in all_items])
    for combos in itertools.product([0,1],repeat=5):
        sum2 = sum([big_candidates[powers_of_2[i]]for i in range(5) if combos[i]==1])
        if sum2==remainder:
            total_hits +=1
            if max(all_items)<46 and max([powers_of_2[i] for i in range(5) if combos[i] ==1])<46:
                print(all_items, [powers_of_2[i] for i in range(5) if combos[i] ==1])

print(total_hits)

