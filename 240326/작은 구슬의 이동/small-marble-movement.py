n, t = map(int, input().split())
x, y, d = input().split()
x = int(x)-1; y = int(y)-1

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

mapper = {
    'R': 0,
    'D': 1,
    'U': 2,
    'L': 3
}

dxs = [0, 1, -1,  0] # 상 우 좌 하
dys = [1, 0,  0, -1]

move_dir = mapper[d]

for i in range(t):
    nx, ny = x + dxs[move_dir], y + dys[move_dir]
    if in_range(nx, ny):
        x, y = nx, ny
    else:
        move_dir = 3 - move_dir

print(x+1, y+1)