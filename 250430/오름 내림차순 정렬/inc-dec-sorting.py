n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()
print(*nums)
re_num = nums[::-1]
print(*re_num)