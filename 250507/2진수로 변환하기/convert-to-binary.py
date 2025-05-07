n = int(input())
# Please write your code here.
answer = []
while True:
    if n < 2:
        answer.append(n)
        break
    answer.append(n % 2)
    n //= 2
    
for x in answer[::-1]:
    print(x, end='')
