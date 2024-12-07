#Part 1

Data = open('Day4Input.txt').read().split('\n')

#convert to numpy array
import numpy as np
N = len(Data)
Array = np.zeros((N,N),dtype='str')
for i in range(N):
    for j in range(N):
        Array[i,j] = Data[i][j]

counter = 0
#search for XMAS or SAMX in rows
for r in Array:
    for i in range(len(r)-3):
        if r[i]+r[i+1]+r[i+2]+r[i+3] == 'XMAS':
            counter += 1
        if r[i]+r[i+1]+r[i+2]+r[i+3] == 'SAMX':
            counter += 1

#search for XMAS or SAMX in columns
for r in Array.T:
    for i in range(len(r)-3):
        if r[i]+r[i+1]+r[i+2]+r[i+3] == 'XMAS':
            counter += 1
        if r[i]+r[i+1]+r[i+2]+r[i+3] == 'SAMX':
            counter += 1

#search for XMAS or SAMX on diagonals
for k in range(-(N-3),(N-3),1):
    d = np.diag(Array,k)
    for i in range(len(d)-3):
        if d[i]+d[i+1]+d[i+2]+d[i+3] == 'XMAS':
            counter += 1
        if d[i]+d[i+1]+d[i+2]+d[i+3] == 'SAMX':
            counter += 1
    d2 = np.diag(np.fliplr(Array),k)
    for i in range(len(d2)-3):
        if d2[i]+d2[i+1]+d2[i+2]+d2[i+3] == 'XMAS':
            counter += 1
        if d2[i]+d2[i+1]+d2[i+2]+d2[i+3] == 'SAMX':
            counter += 1

print(counter)

#Part 2

Data = open('Day4Input.txt').read().split('\n')

#convert to numpy array
import numpy as np
N = len(Data)
A = np.zeros((N,N),dtype='str')
for i in range(N):
    for j in range(N):
        A[i,j] = Data[i][j]

counter = 0
#search for X-MAS in rows [:,N-2]
for i in range(N-2):
    r = A[i]
    for j in range(len(r)-2):
        if A[i,j] == 'M' and A[i+2,j] == 'S' and A[i+1,j+1] == 'A' and A[i,j+2] == 'M' and A[i+2,j+2] == 'S':
            counter += 1
        elif A[i,j] == 'M' and A[i+2,j] == 'M' and A[i+1,j+1] == 'A' and A[i,j+2] == 'S' and A[i+2,j+2] == 'S':
            counter += 1
        elif A[i,j] == 'S' and A[i+2,j] == 'M' and A[i+1,j+1] == 'A' and A[i,j+2] == 'S' and A[i+2,j+2] == 'M':
            counter += 1
        elif A[i,j] == 'S' and A[i+2,j] == 'S' and A[i+1,j+1] == 'A' and A[i,j+2] == 'M' and A[i+2,j+2] == 'M':
            counter += 1

print(counter)
