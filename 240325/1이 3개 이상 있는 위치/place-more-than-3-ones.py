n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0] # 동 남 서 북

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

cnt = 0
for i in range(n):
    for j in range(n):
        tmp = 0
        for dx, dy in zip(dxs, dys):
            nx, ny = i + dx, j + dy
            if in_range(nx, ny) and arr[nx][ny] == 1:
                tmp += 1
        if tmp >= 3:
            cnt += 1



print(cnt)