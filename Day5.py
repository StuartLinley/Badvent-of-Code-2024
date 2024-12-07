#Part 1

import numpy as np
Orders = open('Day5Orders.txt').read().split('\n')

B = []
A = []
for i in Orders:
    B.append(int(i[:2]))
    A.append(int(i[3:]))

B = np.array(B)
A = np.array(A)

Data = open('Day5Pages.txt').read().split('\n')

Pages = []
for i in Data:
    PageNums = i.split(',')
    List = []
    for j in PageNums:
        List.append(int(j))
    Pages.append(List)

mids = []
wrongs = []

for p in Pages:
    OOO = False

    #create sub-lists with only rules we care about
    sub_A = np.array([])
    sub_B = np.array([])
    for j in range(len(p)):
        sub_A = np.append(sub_A,np.where(A == p[j]))
        sub_B = np.append(sub_B,np.where(B == p[j]))

    sub_A = np.unique(sub_A)
    sub_B = np.unique(sub_B)
    intersection = np.intersect1d(sub_A,sub_B)

    sub_A = np.array([])
    sub_B = np.array([])
    for j in range(len(intersection)):
        sub_A = np.append(sub_A,A[int(intersection[j])])
        sub_B = np.append(sub_B,B[int(intersection[j])])

    #Check if first page in in order    
    for j in range(len(p)):
        if j == 0:
            if p[j] in sub_A:
                wrongs.append(p)
                break

        #Check if previous pages are always before
        A_indices = np.where(sub_A == p[j])[0]
        
        for i in range(len(A_indices)):
            a = A_indices[i]
            if sub_B[a] in p[:j]:
                continue
            else:
                OOO = True
                break

        #Check if subsequent pages are always after
        B_indices = np.where(sub_B == p[j])[0]
        
        for i in range(len(B_indices)):
            b = B_indices[i]
            # print(B_indices[0][i])
            # print(A[b])
            if sub_A[b] in p[j+1:]:
                continue
            else:
                OOO = True
                break

        if OOO:
            wrongs.append(p)
            break

        if j == len(p)-1:
            mids.append(p[j//2])

print(f'The number of correctly ordered pages is {len(mids)}')
print(f'The number of incorrectly ordered pages is {len(wrongs)}')
print(np.sum(mids))

#Part 2

mids = []
for p in wrongs:

    #create sub-lists with only rules we care about
    sub_A = np.array([])
    sub_B = np.array([])
    for j in range(len(p)):
        sub_A = np.append(sub_A,np.where(A == p[j]))
        sub_B = np.append(sub_B,np.where(B == p[j]))

    sub_A = np.unique(sub_A)
    sub_B = np.unique(sub_B)
    intersection = np.intersect1d(sub_A,sub_B)

    sub_A = np.array([])
    sub_B = np.array([])
    for j in range(len(intersection)):
        sub_A = np.append(sub_A,A[int(intersection[j])])
        sub_B = np.append(sub_B,B[int(intersection[j])])

    reordered = []
    #find first page
    for j in range(len(p)):
        if p[j] not in sub_A:
            reordered.append(p[j])

    #Rank pages based on the number of times they occur in each list
    unique,counts = np.unique(sub_A,return_counts=True)

    #Put them in order according to the number of times they occur
    for i in range(1,len(counts)):
        index = np.where(counts==i)[0][0]
        reordered.append(int(unique[index]))
    
    #find last page
    for j in range(len(p)):
        if p[j] not in sub_B:
            reordered.append(p[j])
        
    mids.append(reordered[(len(p)-1)//2])

print(np.sum(mids))
