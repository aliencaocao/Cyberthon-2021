from random import randint

data = open('flag.txt', 'rb').read().strip()

data1 = data[::2]
data2 = data[1::2]
data3 = []

assert len(data1) == len(data2)

for i, j in zip(data1, data2):
    data3.append(i ^ j)

output = []

if (randint(0, 1000) % 2):
    print('aaand... data1 is gone!')
    for i, j in zip(data2, data3):
        output.append(j)
        output.append(i)
    open('flag.corrupted', 'wb').write(bytes(output))
else:
    print('aaand... data2 is gone!')
    for i, j in zip(data1, data3):
        output.append(i)
        output.append(j)
    open('flag.corrupted', 'wb').write(bytes(output))
