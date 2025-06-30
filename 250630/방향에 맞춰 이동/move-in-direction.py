n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.

x, y = 0,0

# 동, 서, 남, 북 순으로 dx,dy를 정의한다.
dx = [1,-1,0,0]
dy = [0,0,-1,1]

c_dir_dic = {'E':0, 'W':1, 'S':2, 'N':3}

for i in range(n):
    move_dir = c_dir_dic[dir[i]]
    x += dx[move_dir] * dist[i]
    y += dy[move_dir] * dist[i]

print(x, y)