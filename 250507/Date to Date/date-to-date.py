# num_of_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
# # 시간에서는 상수 60이 쓰이지만 날짜에서는 배열의 인덱스를 이용한다는 개념을 이용


# m = 5
# d = 2

# while True: # 그러나 6월은 30일이므로 매월 마다 적음
#     if m == 7 and d == 5:
#         break

#     d += 1

#     if d > num_of_days[m]:
#         m += 1
#         d = 1
  
# 달마다 조건을 적으면 코드는 이쁘지가 않음 
# 구현 팁 - 조건을 묶기가 어려움
# if ...
# if ...
# if ...
# if ...
num_of_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
cnt = 1 # 날짜이기 때문에 1로 시작
m, d, m2, d2 = map(int, input().split())
# Please write your code here.
while True:
    if m == m2 and d == d2:
        break
    d += 1
    cnt += 1
    if d > num_of_days[m]:
        m += 1
        d = 1
print(cnt)
    
    



