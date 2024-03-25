N = int(input())
lst = []
for _ in range(N):
    d, v = input().split()
    v = int(v)
    lst.append((d, v))

dx = [1, -1, 0, 0] # 동, 서, 남, 북
dy = [0, 0, -1, 1] # 동, 서, 남, 북

x, y = 0, 0
for d, v in lst:
    if d == 'E':
        x += v * dx[0]
        y += v * dy[0]
    elif d == 'W':
        x += v * dx[1]
        y += v * dy[1]
    elif d == 'S':
        x += v * dx[2]
        y += v * dy[2]
    elif d == 'N':
        x += v * dx[3]
        y += v * dy[3]

print(x, y)