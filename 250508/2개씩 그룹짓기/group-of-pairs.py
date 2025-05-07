n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
min_num = []
max_num = []

nums.sort()

for i in range(n):
    min_num.append(nums[i])
    max_num.append(nums[-(i + 1)])

group_sums = [min_num[i] + max_num[i] for i in range(n)]

result = max(group_sums)

print(result)
