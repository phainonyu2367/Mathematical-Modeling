with open('data2_2.md') as fp:
    L1 = []; L2 = []
    for line in fp:
        L1.append(len(line))
        L2.append(len(line.strip()))
data = [str(num) + '\t' for num in L2]
print(L1); print(L2)
with open('data2_2.md', 'a') as fp2:
    fp2.writelines(data)
