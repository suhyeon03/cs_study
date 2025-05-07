arr = list(map(int, input().split()))

arr_1 = []

for i in arr:
    if i == 0:
        break
    arr_1.append(i)

sum_arr = sum(arr_1)
avg_arr = sum(arr_1) / len(arr_1)
print(sum_arr, round(avg_arr, 0))

    
        

