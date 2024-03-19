OFFSET = 1000
MAX_R = 2000

A, B, M = [], [], []

x1, y1, x2, y2 = map(int, input().split())
A.append((x1, y1, x2, y2))
x1, y1, x2, y2 = map(int, input().split())
B.append((x1, y1, x2, y2))
x1, y1, x2, y2 = map(int, input().split())
M.append((x1, y1, x2, y2))

rect = [[0]*(MAX_R + 1) for _ in range(MAX_R + 1)]

for x1, y1, x2, y2 in A:
    x1 += OFFSET
    y1 += OFFSET
    x2 += OFFSET
    y2 += OFFSET
    for x in range(x1, x2):
        for y in range(y1, y2):
            rect[x][y] += 1

for x1, y1, x2, y2 in B:
    x1 += OFFSET
    y1 += OFFSET
    x2 += OFFSET
    y2 += OFFSET
    for x in range(x1, x2):
        for y in range(y1, y2):
            rect[x][y] += 1

for x1, y1, x2, y2 in M:
    x1 += OFFSET
    y1 += OFFSET
    x2 += OFFSET
    y2 += OFFSET
    for x in range(x1, x2):
        for y in range(y1, y2):
            rect[x][y] += 10

area = 0
for x in range(MAX_R + 1):
    for y in range(MAX_R + 1):
        if rect[x][y] >= 10:
            rect[x][y] = 0
        elif rect[x][y] >= 1:
            area += 1
        else:
            pass

print(area)