fin = '/Users/Jeremy/Desktop/p098_words.txt'

io = open(fin)

l = io.readline()

words = []

while l:
    words.append(l)
    l = io.readline()

words = words[0].replace('"','').split(',')

pairs = []

for i in range(len(words)-1):
    for j in range(i+1,len(words)):
        if sorted(words[i]) == sorted(words[j]):
            pairs.append([words[i],words[j]])

print(pairs)

pairs = sorted(pairs, key = lambda x:-len(x[0]))
print(pairs)

for p in pairs:
    l = len(set(p[0]))
    bottom = int(10**((l-1)/2))
    top = int(10**(l/2) + 1)
    current_candidates = []
    for i in range(bottom,top):
        s = i*i
        if len(set(str(s)))==l:
            current_candidates.append(s)
    for i in range(len(current_candidates)-1):
        n1_str = str(current_candidates[i])
        key = {n1_str[ii]:p[0][ii] for ii in range(len(n1_str))}
        stop = False
        for ii in range(len(n1_str)):
            if key[n1_str[ii]] != p[0][ii]:stop=True
        if stop:continue
        for j in range(i+1,len(current_candidates)):
            n2_str = str(current_candidates[j])
            try:
                new_word = ''.join([key[s] for s in n2_str])
            except:
                continue
            if new_word == p[1]:print('YAY',n1_str,n2_str,p[0],p[1])





