
x = []
n = int(input('no of elements in 1st list: '))

for i in range(0, n):
    num = int(input('enter {} no: '.format(i + 1)))
    x.append(num)


y = []
m = int(input('no of elements in 2nd list: '))

for j in range(0, m):
    num2 = int(input('enter {} no.: '.format(j)))
    y.append(num2)

print('first list is: {}'.format(x))
print('2nd list is {}'.format(y))


z = []
for k in range(0, n):
    if x[k] % 2 != 0:
        z.append(x[k])

for l in range(0, m):
    if y[l] % 2 == 0:
        z.append(y[l])

print('merge list is: {}'.format(z))
