# 시간의 흐름
# 진법 변환
# 선분의 표현 - 카운팅 배열

# 수학적인 풀이 - 시침과 분침이 만나는
# 0 0 
# 0 1
# 0 2
# 0 3
# ....
# 24 00
# 분침이 더 앞으로 갔다면 만났다고 생각한다.
# 시침은 하루동안 2번 돈다, 분침은 24번 돈다 -> 22번 만난다.
# 12 x 60, 720칸으로 쪼갠다. 분침 -> 12칸 , 시침은 -> 1칸
# h = 0
# m = 0
# anser = 0 
# for i in range(24 * 60):
#     if m < h and m + 12 >= h + 1: 
#         answer += 1  
#     h += 1
#     m += 12
    

# h = 2
# m = 5

# cnt = 0
# # while not (h == 4 and m == 1):
# while True:
#     if h == 4 and m == 1:
#         break
#     m += 1
#     cnt += 1
#     if m == 60:
#         h += 1
#         m = 0
# print(cnt)
    
#     # 2:59
#     # 2:60 -> 3:00

h, m, h2, m2 = map(int, input().split())
cnt = 0
# Please write your code here.
while True:
    if h == h2 and m == m2:
        break
    m += 1
    cnt += 1

    if m == 60:
        h += 1
        m = 0
print(cnt)

    