n = int(input())
arr = [0] * 110
for i in range(n):
    x1, x2 = map(int, input().split())
    x1 += 100
    x2 += 100 # 음수가 나오기 뗴문에 조건을 조정
    for j in range(x1, x2):
        arr[j] += 1
answer = 0
for i in range(110):
    if answer < arr[i]:
        answer = arr[i]
print(answer)
