import itertools
def count_paths(r):
    ones = [1] * r + [-1] *r
    for p in itertools.combinations(ones,2*r):
        print(p)

count_paths(3)