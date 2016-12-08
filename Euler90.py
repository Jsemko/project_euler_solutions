import itertools

square_numbers = ['01','04','09','16','25','36','49','64','81']

def good_pair(c1,c2):
    for n in square_numbers:
        if not ((n[0] in c1 and n[1] in c2) or (n[1] in c1 and n[0] in c2)):return False
    return True

digits = '0123456789'

good = 0

for c1 in itertools.combinations(digits,6):
    for c2 in itertools.combinations(digits,6):
        c1 = set(c1)
        c2 = set(c2)
        if '6' in c1:c1.add('9')
        if '9' in c1:c1.add('6')
        if '6' in c2:c2.add('9')
        if '9' in c2:c2.add('6')
        if good_pair(c1,c2):good+=1

print(good/2)
