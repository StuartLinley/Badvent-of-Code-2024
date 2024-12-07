#Part 1

Map = open('Day6Input.txt').read().split('\n')

import numpy as np

M = np.zeros((len(Map),len(Map[0])),dtype='str')

for i in range(len(Map)):
    for j in range(len(Map[0])):
        M[i,j] = Map[i][j]

#Find first position:
start_index = np.where(M == '^')
i = start_index[0][0]
j = start_index[1][0]

import time
from IPython.display import clear_output

while ('^' in M) or ('>' in M) or ('v' in M) or ('<' in M):
    if M[i,j] == '^':
        if i == 0:
            M[i,j] = 'X'
        elif M[i-1,j] == '#':
            M[i,j] = '>'
        else:
            M[i,j] = 'X'
            M[i-1,j] = '^'
            i = i-1

    elif M[i,j] == '>':
        if j == len(Map[0])-1:
            M[i,j] = 'X'
        elif M[i,j+1] == '#':
            M[i,j] = 'v'
        else:
            M[i,j] = 'X'
            M[i,j+1] = '>'
            j = j+1

    elif M[i,j] == 'v':
        if i == len(Map)-1:
            M[i,j] = 'X'
        elif M[i+1,j] == '#':
            M[i,j] = '<'
        else:
            M[i,j] = 'X'
            M[i+1,j] = 'v'
            i = i+1

    elif M[i,j] == '<':
        if j == 0:
            M[i,j] = 'X'
        elif M[i,j-1] == '#':
            M[i,j] = '^'
        else:
            M[i,j] = 'X'
            M[i,j-1] = '<'
            j = j-1

counter = 0
for i in range(len(Map)):
    for j in range(len(Map[0])):
        if M[i,j] == 'X':
            counter += 1

print(f'The guard visited {counter} distinct positions.')

#Part 2

def CheckForLoop(i,j,d,Map):
    M = Map.copy()

    #insert obstacle:
    if d == '^':
        M[i-1,j] = '#'
    elif d == '>':
        M[i,j+1] = '#'
    elif d == 'v':
        M[i+1,j] = '#'
    elif d == '<':
        M[i,j-1] = '#'

    #Initialize tracker (D,i,j) where D is direction (0 = ^, 1 = >, 2 = v, 3 = <) and i,j are row,column indices
    Ps = np.zeros((0,3),dtype='int')


    while ('^' in M) or ('>' in M) or ('v' in M) or ('<' in M):
    
        if M[i,j] == '^':
            if np.any(np.all(np.array([0,i,j]) == Ps, axis = 1)):
                return True
            Ps = np.vstack((Ps,np.array([0,i,j])))
            if i == 0:
                M[i,j] = 'X'
            elif M[i-1,j] == '#':
                M[i,j] = '>'
            else:
                M[i,j] = 'X'
                M[i-1,j] = '^'
                i = i-1
    
        elif M[i,j] == '>':
            if np.any(np.all(np.array([1,i,j]) == Ps, axis = 1)):
                return True
            Ps = np.vstack((Ps,np.array([1,i,j])))
            if j == M.shape[1]-1:
                M[i,j] = 'X'
            elif M[i,j+1] == '#':
                M[i,j] = 'v'
            else:
                M[i,j] = 'X'
                M[i,j+1] = '>'
                j = j+1
    
        elif M[i,j] == 'v':
            if np.any(np.all(np.array([2,i,j]) == Ps, axis = 1)):
                return True
            Ps = np.vstack((Ps,np.array([2,i,j])))
            if i == M.shape[0]-1:
                M[i,j] = 'X'
            elif M[i+1,j] == '#':
                M[i,j] = '<'
            else:
                M[i,j] = 'X'
                M[i+1,j] = 'v'
                i = i+1
    
        elif M[i,j] == '<':
            if np.any(np.all(np.array([3,i,j]) == Ps, axis = 1)):
                return True
            Ps = np.vstack((Ps,np.array([3,i,j])))
            if j == 0:
                M[i,j] = 'X'
            elif M[i,j-1] == '#':
                M[i,j] = '^'
            else:
                M[i,j] = 'X'
                M[i,j-1] = '<'
                j = j-1

    return False

Map = open('Day6Input.txt').read().split('\n')

import numpy as np

M = np.zeros((len(Map),len(Map[0])),dtype='str')

for i in range(len(Map)):
    for j in range(len(Map[0])):
        M[i,j] = Map[i][j]

#Find first position:
start_index = np.where(M == '^')
i = start_index[0][0]
j = start_index[1][0]
i0 = i.copy()
j0 = j.copy()

import time
from IPython.display import clear_output

inf = 0
P_O = np.zeros([0,2],dtype='int')
P_O = np.vstack((P_O,np.array([i,j])))

while ('^' in M) or ('>' in M) or ('v' in M) or ('<' in M):
    if M[i,j] == '^':
        if i == 0:
            M[i,j] = 'X'
        elif M[i-1,j] == '#':
            M[i,j] = '>'
        else:
            if CheckForLoop(i,j,'^',M) and np.any(np.all(np.array([i-1,j]) == P_O, axis = 1)) == False and M[i-1,j] != 'X':
                P_O = np.vstack((P_O,np.array([i-1,j])))
                inf += 1
            M[i,j] = 'X'
            M[i-1,j] = '^'
            i = i-1

    elif M[i,j] == '>':
        if j == len(Map[0])-1:
            M[i,j] = 'X'
        elif M[i,j+1] == '#':
            M[i,j] = 'v'
        else:
            if CheckForLoop(i,j,'>',M) and np.any(np.all(np.array([i,j+1]) == P_O, axis = 1)) == False and M[i,j+1] != 'X':
                P_O = np.vstack((P_O,np.array([i,j+1])))
                inf += 1
            M[i,j] = 'X'
            M[i,j+1] = '>'
            j = j+1

    elif M[i,j] == 'v':
        if i == len(Map)-1:
            M[i,j] = 'X'
        elif M[i+1,j] == '#':
            M[i,j] = '<'
        else:
            if CheckForLoop(i,j,'v',M) and np.any(np.all(np.array([i+1,j]) == P_O, axis = 1)) == False and M[i+1,j] != 'X':
                P_O = np.vstack((P_O,np.array([i+1,j])))
                inf += 1
            M[i,j] = 'X'
            M[i+1,j] = 'v'
            i = i+1

    elif M[i,j] == '<':
        if j == 0:
            M[i,j] = 'X'
        elif M[i,j-1] == '#':
            M[i,j] = '^'
        else:
            if CheckForLoop(i,j,'<',M) and np.any(np.all(np.array([i,j-1]) == P_O, axis = 1)) == False and M[i,j-1] != 'X':
                P_O = np.vstack((P_O,np.array([i,j-1])))
                inf += 1
            M[i,j] = 'X'
            M[i,j-1] = '<'
            j = j-1

counter = 0
for i in range(len(Map)):
    for j in range(len(Map[0])):
        if M[i,j] == 'X':
            counter += 1

print(f'The guard visited {counter} distinct positions.')
print(f'There are {inf} possible obstacle locations that will create infinite loops')
