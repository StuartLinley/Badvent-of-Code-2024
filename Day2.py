#Part 1
Data = open('Day2Input.txt')

lines = Data.readlines()

unsafe = 0
for i in lines:
    stringline = i.split(" ")
    line = []
    for j in stringline:
        line.append(int(j))

    diff = []
    for k in range(len(line)-1):
        diff.append(line[k+1]-line[k])

    for l in range(len(diff)-1):
        if diff[l] * diff[l+1] < 0:
            unsafe += 1
            break
        elif abs(diff[l]) < 1 or abs(diff[l]) > 3:
            unsafe += 1
            break
        elif abs(diff[l+1]) < 1 or abs(diff[l+1]) > 3:
            unsafe += 1
            break

print(f'The number of unsafe reports is {unsafe}')
print(f'The number of safe reports is {len(lines)-unsafe}')

#Part 2
Data = open('Day2Input.txt')

lines = Data.readlines()

safe = 0
for i in lines:
    stringline = i.split(" ")
    line = []
    for j in stringline:
        line.append(int(j))

    faults = []
    for e in range(len(line)):
        line_copy = line.copy()
        line_copy.pop(e)
        
        diff = []
        for k in range(len(line_copy)-1):
            diff.append(line_copy[k+1]-line_copy[k])

        faulted = 0
        for l in range(len(diff)-1):
            if diff[l] * diff[l+1] < 0:
                faulted = 1
                break
            elif abs(diff[l]) < 1 or abs(diff[l]) > 3:
                faulted = 1
                break
            elif abs(diff[l+1]) < 1 or abs(diff[l+1]) > 3:
                faulted = 1
                break
        
        faults.append(faulted)

    for f in faults:
        if f == 0:
            safe += 1
            break

print(f'The number of safe reports is {safe}')
print(f'The number of unsafe reports is {len(lines)-safe}')
