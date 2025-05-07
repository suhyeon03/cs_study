arr = list(map(int, input().split()))
arr_1 = []
cnt = 0
for i in arr:
    if i == 0:
        break
    arr_1.append(i)

for i in range(1,10):
    cnt = 0
    for j in arr_1:
        if j // 10 == i:
            cnt += 1
    print(f'{i} - {cnt}')
