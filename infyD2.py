def nonemat(a):
    for task in a:
        for i in range(task[1]):
            temp = task[0][-1]
            task[0] = temp + task[0][:-1]
        #print(task)

        tempans = ''
        for i in range(1, len(task[0]), 2):
            temp = task[0][i].lower()
            #print(temp)
            if temp in ('a', 'e', 'i', 'o', 'u'):
                continue
            tempans += task[0][i]
        if tempans != '':
            print(tempans, end = ',')

c = int(input())
a = []
for _ in range(c):
    ab = input()
    x, y = ab.split(',')
    a.append([x, int(y)])

print(a)
nonemat(a)

