n = 4
arr = []
for i in range(n):
    x = list(map(int, input().split()))

    arr.append(x)

for i in range(n):
    total = 0
    for j in range(n):
        total += arr[i][j]
    print(total)

# arr = [list(map(int, input().split())) for i in range (n)]
# for i in range(n):
#    for j in range(n):
#       print(arr[i][j], end='')
#    print()