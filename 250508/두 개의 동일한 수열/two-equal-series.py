n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
# 변수 선언 및 입력
def equal():
    # n개의 원소를 순서대로 봤을 때
    # 전부 동일한 경우에만 일치합니다.
    # 단 하나라도 다르다면, false입니다.
    for elem1, elem2 in zip(A, B):
        if elem1 != elem2:
            return False
    
    return True


# 정렬
A.sort()
B.sort()

# 수열이 일치하는지 확인합니다.
if equal():
    print("Yes")
else:
    print("No")

        



    