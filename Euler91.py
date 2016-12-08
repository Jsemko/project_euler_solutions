width = 50


total = width * width

for x1 in range(width+1):
    for y1 in range(width+1):
        for x2 in range(width+1):
            for y2 in range(width+1):
                if x1==x2 and y1==y2:continue
                if x1==0 and y1==0:continue
                if x2==0 and y2==0:continue
                dy,dx = y2 - y1,x2-x1
                if dy*y1 + dx*x1 == 0:
                    total+=1

print(total)

