# arr = []
# for i in range(5):
#     x = [0] * 10
#     arr.append(x)

# arr = [[0] * 10 for i in range(5)]
# arr = [[0 for i in range(10)] for i in range(5)]

# arr = [[0]*10] * 5 # 얕은 복사 독립적으로 사용이 안된다.

n,m = map(int, input().split())
arr = [[0]*m for i in range(n)]

value = 1
for i in range(n):
    for j in range(m):
        arr[i][j] = value
        value += 1

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()
