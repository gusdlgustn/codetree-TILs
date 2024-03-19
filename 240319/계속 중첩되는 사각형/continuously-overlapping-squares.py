OFFSET = 100
MAX_R = 200

n = int(input())

rect = []
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x1 += OFFSET
    y1 += OFFSET
    x2 += OFFSET
    y2 += OFFSET
    rect.append((x1, y1, x2, y2))


color = [[0]*(MAX_R + 1) for _ in range(MAX_R + 1)]

for i, (x1, y1, x2, y2) in enumerate(rect):
    if i % 2 == 0: #빨간색
        for x in range(x1, x2):
            for y in range(y1, y2):
                color[x][y] = 'R'

    elif i % 2 != 0: #파란색
        for x in range(x1, x2):
            for y in range(y1, y2):
                color[x][y] = 'B'

area = 0

for x in range(MAX_R + 1):
    for y in range(MAX_R + 1):
        if color[x][y] == 'B':
            area += 1

print(area)