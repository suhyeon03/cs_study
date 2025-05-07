arr = input().split()

sum_arr = 0
for i in arr:
    sum_arr += float(i)
avg_sum = round(sum_arr/8, 1)
print(avg_sum)

