# 3
# 251
# 472
# 893

# color = [0] * 50

# q = int(input())
# for i in range(0):
#     s, e, c = map(int, input().split())

#     for j in range()
#         color[j] = c

n, k = map(int, input().split())
arr = [0] * (n+1) 
# Please write your code here.
for i in range(k):
    a, b = map(int, input().split())

    for j in range(a, b+1):
        arr[j] += 1

answer = 0
for i in range(1, n+1):
    if answer < arr[i]:
        answer = arr[i]
print(answer)