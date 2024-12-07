#Part 1
#------------------------------------------------------------------------------------------------------------------#
Input = open('Day7Input.txt').read().split('\n')

#Import data and set variables:
#O: a list of output values
#E: an (Nx1) array of lists where each list contains the numbers in the equation

O = []
List = []

for i in Input:
    j = i.split(':')
    O.append(int(j[0]))
    List.append(j[1])

import numpy as np

E = np.zeros((0,1),dtype='object')

for l in range(len(List)):
    Nums = []
    m = List[l].split(' ')
    for q in m:
        if q.isdigit():
            Nums.append(int(q))

    E = np.vstack((E,[0]))
    E[l,0] = Nums       

def GetPerm(m):
    n = int(2**m)
    A = np.zeros((n,m))
    v = np.linspace(0,n-1,n,dtype='int')
    binary_repr_v = np.vectorize(np.binary_repr)
    b = binary_repr_v(v)
    
    for i in range(n):
        for j in range(len(b[i])):
            A[i,-1-j] = b[i][-1-j]

    return A

Sum = 0
for i in range(len(O)):
    Nums = E[i,0]
    n = len(Nums)-1
    Ops = GetPerm(n)

    for j in range(Ops.shape[0]):
        Test = Ops[j]
        Output = Nums[0]
        for k in range(len(Test)):
            if Test[k] == 0:
                Output = Output + Nums[k+1]
            else:
                Output = Output * Nums[k+1]

        if Output == O[i]:
            Sum = Sum + O[i]
            break
                
print(Sum)        


#------------------------------------------------------------------------------------------------------------------#
#Part 2                                                                                                            #
#------------------------------------------------------------------------------------------------------------------#

def GetPermEDuFUCK(m,b):
    n = int(b**m)
    A = np.zeros((n,m))
    v = np.linspace(0,n-1,n,dtype='int')
    base_repr_v = np.vectorize(np.base_repr)
    based_v = base_repr_v(v,base = b)
    
    for i in range(n):
        for j in range(len(based_v[i])):
            A[i,-1-j] = based_v[i][-1-j]

    return A

Sum = 0
for i in range(len(O)):
    Nums = E[i,0]
    n = len(Nums)-1
    Ops = GetPermEDuFUCK(n,3)

    for j in range(Ops.shape[0]):
        Test = Ops[j]
        Output = Nums[0]
        for k in range(len(Test)):
            if Test[k] == 0:
                Output = Output + Nums[k+1]
            elif Test[k] == 1:
                Output = Output * Nums[k+1]
            else:
                Output = int(str(Output)+str(Nums[k+1]))

        if Output == O[i]:
            Sum = Sum + O[i]
            break
                
print(Sum)        
