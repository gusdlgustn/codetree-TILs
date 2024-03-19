OFFSET = 100
MAX_R = 200

N = int(input())
lst = []

for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    lst.append((x1, y1, x2, y2))

square = [[0] * (MAX_R + 1) for _ in range(MAX_R + 1)]

for x1, y1, x2, y2 in lst:
    x1, y1 = x1 + OFFSET, y1 + OFFSET
    x2, y2 = x2 + OFFSET, y2 + OFFSET

    for i in range(x1, x2):
        for j in range(y1, y2):
            square[i][j] = 1

area = 0
for x in range(0, MAX_R + 1):
    for y in range(0, MAX_R + 1):
        if square[x][y]:
            area += 1

print(area)