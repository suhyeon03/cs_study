n = int(input())
arr = list(map(int, input().split()))
cnt = [0 for i in range(10)]

for i in range(n):
    cnt[arr[i]] += 1
for i in range(1,10):
    print(cnt[i])

# for i in range(1,10):
#     cnt = 0
#     for j in range(n):
#         if  arr[j] == i:
#             cnt += 1
#     print(cnt)