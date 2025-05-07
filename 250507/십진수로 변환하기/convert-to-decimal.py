# binary = [1,1,1,0,1]

# # Please write your code here.
# val = 1
# answer = 0

# for x in binary[::-1]:
#     answer += x * val
#     val *= 2 
# print(answer)

# 이진수 뒤에다 0을 붙이면 2배, 10진수 뒤에다 0을 붙이면 10배
binary = [1,1,1,0,1]

answer = 0

for x in binary:
    answer *= 2
    answer += x
print(answer)
