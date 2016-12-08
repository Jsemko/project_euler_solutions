def is_square(n):
    return round(n**.5)**2 == n


all_pairs = list()

for i in range(1,100):
    for j in range(i+1,100000):
        if is_square(i**2 +i*j+j**2):
            print(i,j)

print(len(all_pairs))