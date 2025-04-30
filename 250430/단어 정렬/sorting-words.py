n = int(input())
word = [input() for _ in range(n)]

# Please write your code here.
sorted_arr = sorted(word)
for i in sorted_arr:
    print(i)