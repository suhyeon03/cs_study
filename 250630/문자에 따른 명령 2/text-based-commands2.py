dirs = input()

# Please write your code here.
x, y = 0, 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dir = 0  # 시작 방향: 북쪽

for cmd in dirs:
    if cmd == 'L':
        dir = (dir - 1 + 4) % 4  # 왼쪽 회전
    elif cmd == 'R':
        dir = (dir + 1) % 4      # 오른쪽 회전
    elif cmd == 'F':
        x += dx[dir]
        y += dy[dir]

print(x, y)




