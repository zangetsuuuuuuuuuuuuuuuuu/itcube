x = int(input())
n = 7
count = 0
maximum = 1000
for j in range(1, n + 1):
    if x // 4 == 0:
        count += 1
        if x < maximum:
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')
