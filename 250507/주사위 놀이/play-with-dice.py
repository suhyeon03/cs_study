arr = list(map(int, input().split()))
cnt = 0

for i in range(1,7):
    cnt = 0
    for j in arr:
        if j == i:
            cnt += 1

    print(f'{i} - {cnt}')

