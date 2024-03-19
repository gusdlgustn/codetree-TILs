OFFSET = 100
MAX_R = 200

N = int(input())

vertex = []
for _ in range(N):
    x, y = tuple(map(int, input().split()))
    vertex.append((x, y))

rect = [[0]*(MAX_R + 1) for _ in range(MAX_R + 1)]

for x, y in vertex:
    x += OFFSET
    y += OFFSET
    for r in range(x, x+8):
        for c in range(y, y+8):
            rect[r][c] += 1

area = 0
for r in range(MAX_R + 1):
    for c in range(MAX_R + 1):
        if rect[r][c] > 0:
            area += 1

print(area)