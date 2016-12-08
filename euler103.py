i1 = 15
m = 700
import itertools


for i2 in range(i1+1, 65):
    for i3 in range(i2+1,66):
        for i4 in range(i3+1,67):
            for i5 in range(i4+1,68):
                for i6 in range(i5+1,69):
                    for i7 in range(i6+1,70):
                        if i7 >= i1+i2:continue
                        if i7 + i6 >= i1+i2+i3:continue
                        if i7 + i6 + i5 >= i1+i2 + i3  + i4: continue
                        if i7 + i6 + i5 + i1+i2 + i3  + i4 < m:
                            allthem = [i1,i2,i3,i4,i5,i6,i7]
                            my_sums = []
                            for s in itertools.combinations(allthem,2):
                                my_sums.append(sum(s))
                            if len(my_sums) > len(set(my_sums)):continue
                            for s in itertools.combinations(allthem,3):
                                my_sums.append(sum(s))
                            if len(my_sums) > len(set(my_sums)): continue
                            for s in itertools.combinations(allthem, 4):
                                my_sums.append(sum(s))
                            if len(my_sums) > len(set(my_sums)): continue

                            m = i7 + i6 + i5 + i1+i2 + i3  + i4
                            print(i1,i2,i3,i4,i5,i6,i7)