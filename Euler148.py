p = 7
row = 1000000000

tri = (p+1)*p //2

import numpy as np




def get_count(r):
    first_divisor = int(np.log(r) / np.log(p))
    if not first_divisor:
        return (r +1)*r //2
    n_tri = r // (p ** first_divisor)
    remainder = r % (p ** first_divisor)

    total = ((n_tri+1)*n_tri //2)*tri ** first_divisor
    if remainder:
        total += (n_tri+1) * get_count(remainder)
    return total

print(get_count(row))