n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# Please write your code here.

mapper = {
    'R': 0,
    'D': 1,
    'U': 2,
    'L': 3
}
r, c, d = int(r) - 1, int(c) - 1, mapper[d]

dxs = [0, 1, -1,  0]
dys = [1, 0,  0, -1]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

for _ in range(t):
    nx, ny = r + dxs[d], c + dys[d]
    
    if in_range(nx, ny):
        r, c = nx, ny
    
    else:
        d = 3 - d

print(r + 1, c + 1)
