str = input()

# Please write your code here.

# sorted_arr = sorted(str)
# sorted_str = ''.join(sorted_arr)
str_1 = list(str)
str_1.sort()
for i in str_1:
    print(i, end='')
