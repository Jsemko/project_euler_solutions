
top = 10**20

goto = int(top ** .5)

def sum_of_digs(n):
    return sum([int(d) for d in str(n)])

all_nums = set()

for i in range(2,100):
    n = i
    while n < top:
        if sum_of_digs(n)==i:
            root = round(n ** (1/i))
            print('{n} = {i} ^ {root}'.format(n=n,i=i,root=root))
            all_nums.add(n)
        n*=i

all_nums = all_nums.difference({2,3,4,5,6,7,8,9})

print(len(all_nums))
print(all_nums)

print(sorted(list(all_nums))[29])

