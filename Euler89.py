
fin = '/Users/Jeremy/Desktop/p089_roman.txt'

io = open(fin)

replace_values = [['DCCCC','CM',3],
                 ['CCCC' ,'CD',2],
                 ['LXXXX','XC',3],
                 ['XXXX' ,'XD',2],
                 ['VIIII','IX',3],
                 ['IIII' ,'IV',2]]

tot = 0
while True:
    l = io.readline()
    if not l:break
    for triple in replace_values:
        while triple[0] in l:
            l = l.replace(triple[0],triple[1])
            tot += triple[2]

print(tot)
