#Part 1
data = open('Day3Input.txt').read()

data1 = data.split(',')

list1 = []
list2 = []

for d in range(len(data1)-1):

    i = data1[d].rfind('mul(')
    
    if data1[d][i+4:].isdigit():
        j = data1[d+1].find(')')
        if j == -1 or j == 0:
            continue
        elif data1[d+1][:j].isdigit():
            list1.append(int(data1[d][i+4:]))
            list2.append(int(data1[d+1][:j]))

sum = 0
for i in range(len(list1)):
    sum = sum + list1[i]*list2[i]    

print(sum)

#Part 2

data = open('Day3Input.txt').read()

data1 = data.split(',')

list1 = []
list2 = []
do = True
for d in range(len(data1)-1):
    
    find_dont = data1[d].find("don't()")
    find_do = data1[d].find("do()")
    if find_dont != -1 and find_do <= find_dont:
        do = False
    elif find_do != -1 and find_dont <= find_do:
        do = True

    i = data1[d].rfind('mul(')
    
    if data1[d][i+4:].isdigit():
        j = data1[d+1].find(')')
        if j == -1 or j == 0:
            continue
        elif data1[d+1][:j].isdigit() and do == True:
            list1.append(int(data1[d][i+4:]))
            list2.append(int(data1[d+1][:j]))

sum = 0
for i in range(len(list1)):
    sum = sum + list1[i]*list2[i]    

print(sum)
