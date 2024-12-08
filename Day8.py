# Part 1

#Import input and cast as a matrix (#Matrices4Life)
Map = open('Day8Input.txt').read().split('\n')

import numpy as np
n = len(Map)
m = len(Map[0])

M = np.zeros((n,m),dtype='str')

for i in range(n):
    for j in range(m):
        M[i,j] = Map[i][j]

#Identify a list of all antenna frequencies
F = np.unique(M)
F = np.delete(F,np.where(F == '.'))

antinodes = np.zeros((0,2),dtype='float')

for f in F:
    #Find all indices of a certain frequency
    fx,fy = np.where(M==f)

    for i in range(len(fx)):
        for j in range(len(fy)):
            if j == i:
                continue
            else:
                #Calculate slope and distance between antennae of same frequency
                slope = (fy[i]-fy[j])/(fx[i]-fx[j])
                d = fx[j] - fx[i]
                
                #Find antinode 1
                an1x = fx[i] + 2*d
                an1y = fy[i] + 2*d*slope
                #If antinode 1 is in the grid, and not already in the list, add it to the list
                if an1x < m and an1x > -1 and an1y < n and an1y > -1 and not np.any(np.all(antinodes == np.array([an1x,an1y]),axis = 1)):
                    antinodes = np.vstack((antinodes,np.array([an1x,an1y])))
                
                #Find antinode 2
                an2x = fx[j] - 2*d
                an2y = fy[j] - 2*d*slope
                #If antinode 2 is in the grid, and not already in the list, add it to the list
                if an2x < m and an2x > -1 and an2y < n and an2y > -1 and not np.any(np.all(antinodes == np.array([an2x,an2y]),axis = 1)):
                    antinodes = np.vstack((antinodes,np.array([an2x,an2y])))

print(f'The number of unique antinodes within the map is {len(antinodes)}')

#Part 2

antinodes = np.zeros((0,2),dtype='float')

for f in F:
    #Find all indices of a certain frequency
    fx,fy = np.where(M==f)

    for i in range(len(fx)):
        for j in range(len(fy)):
            if j == i:
                continue
            else:
                #Calculate slope and distance between antennae of same frequency
                slope = (fy[i]-fy[j])/(fx[i]-fx[j])
                d = fx[j] - fx[i]

                d_forward = np.arange(fx[i],m,d)
                d_backward = np.arange(fx[i]-d,-1,-d)
                dznutz = np.append(d_backward,d_forward)
                
                for p in dznutz:
                    d = fx[i] - p
                    #Find antinode 
                    anx = fx[i] - d
                    any = fy[i] - d*slope
                    #If antinode 1 is in the grid, and not already in the list, add it to the list
                    if anx < m and anx > -1 and any < n and any > -1 and not np.any(np.all(antinodes == np.array([anx,any]),axis = 1)):
                        antinodes = np.vstack((antinodes,np.array([anx,any])))

print(f'The number of unique antinodes, including the effects of resonant harmonics, within the map is {len(antinodes)}')
