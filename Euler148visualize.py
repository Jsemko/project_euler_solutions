import matplotlib.pyplot as plt

N = 1001

current_row = [1]

plt.plot(-1/2,-1,'bo')
count = 1

height = -2

for row in range(2,N):
    next_row = [1]
    for c in range(len(current_row)-1):
        next_row.append(current_row[c]+current_row[c+1])
    next_row.append(1)
    for j in range(len(next_row)):
        if next_row[j] % 7 == 0:
            pass#plt.plot(j +height/2,height,'ro')
        else:
            #plt.plot(j+ height/2,height,'bo')
            count +=1
    height -=1
    current_row = next_row

plt.show()

print(count)