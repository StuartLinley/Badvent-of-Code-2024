#Part 1
import pandas as pd
import numpy as np

Data = pd.read_csv('Day1Input.txt',sep=' ',header=None)

list1 = np.array(Data.values.T[0])
list2 = np.array(Data.values.T[3])

list1_sort = np.sort(list1)
list2_sort = np.sort(list2)

list_diff = np.abs(list1_sort - list2_sort)

list_sum = np.sum(list_diff)

print(f'The sum of the list differences is {list_sum}')

#Part 2
sim_list = np.zeros(len(list1))

for i in range(len(list1)):
    counter = 0
    for j in range(len(list2)):
        if list1[i] == list2[j]:
            counter += 1
    sim_list[i] = counter*list1[i]

similarity = np.sum(sim_list)

print(f'The similarity score for the two lists is {similarity}')
