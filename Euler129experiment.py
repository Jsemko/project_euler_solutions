for i in range(1000001,1100000,2):
    if i % 5 == 0:continue
    d = 2
    n = (10**d-1)//9
    while n % i != 0:
        d+=1
        n *=10
        n+=1
        n = n % i
    print(str(i) + '->' + str(d))