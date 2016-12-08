import numpy as np
transition_matrix = np.zeros((40,40))

sided_die = 4

moves = np.zeros(sided_die*2+1)
for i in range(sided_die):
    moves[i+1] +=i
    moves[-i] +=i
moves[sided_die + 1] = sided_die
moves /= (sided_die **2)

for i in range(40):
    for j in range(len(moves)):
        transition_matrix[i,(i+j) % 40] = moves[j]

print(np.linalg.matrix_power(transition_matrix,500)[:,0])

CC1_index = 2
CC2_index = 17
CC3_index = 33
Jail = 10
G2J = 30
Go = 0

CH1 = 7
CH2 = 22
CH3 = 36
C1 = 11
E3 = 24
H2 = 39
R1 = 5
CH1R = 15
CH2R = 25
CH3R = 5

CH1U = 12
CH2U = 28
CH3U = 12

CH1B = CH1 - 3
CH2B = CH2 - 3
CH3B = CH3 - 3

for i in range(40):
    orig = transition_matrix[i,CH1]
    transition_matrix[i, CH1] = orig * (6/16)
    for index in [Go,Jail,C1,E3,H2,R1,CH1R,CH1R,CH1U, CH1B]:
        transition_matrix[i,index] += orig * 1/16

    orig = transition_matrix[i, CH2]
    transition_matrix[i, CH2] = orig * (6 / 16)
    for index in [Go, Jail, C1, E3, H2, R1, CH2R, CH2R, CH2U, CH2B]:
        transition_matrix[i, index] += orig * 1 / 16

    orig = transition_matrix[i, CH3]
    transition_matrix[i, CH3] = orig * (6 / 16)
    for index in [Go, Jail, C1, E3, H2, R1, CH3R, CH3R, CH3U, CH3B]:
        transition_matrix[i, index] += orig * 1 / 16

print(np.sum(transition_matrix,axis=1))

for i in range(40):
    orig = transition_matrix[i,CC1_index]
    transition_matrix[i, CC1_index] = orig * (14/16)
    transition_matrix[i,Go] += orig * 1/16
    transition_matrix[i,Jail] += orig * 1/16

    orig = transition_matrix[i, CC2_index]
    transition_matrix[i, CC2_index] = orig * (14 / 16)
    transition_matrix[i, Go] += orig * 1 / 16
    transition_matrix[i, Jail] += orig * 1 / 16

    orig = transition_matrix[i, CC3_index]
    transition_matrix[i, CC3_index] = orig * (14 / 16)
    transition_matrix[i, Go] += orig * 1 / 16
    transition_matrix[i, Jail] += orig * 1 / 16

print(np.sum(transition_matrix,axis=1))

transition_matrix *= (35/36)
for i in range(40):
    transition_matrix[i,Jail] += 1/36

ans = np.linalg.matrix_power(transition_matrix,50000)[0,:]
print(ans)

print(np.argsort(-ans))