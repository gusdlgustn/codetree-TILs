n = int(input())

line = []
for i in range(n):
    x1, x2 = map(int, input().split())
    line.append((x1, x2))

overlap = [0]*101

for i in line:
    for j in range(i[0], i[1]+1):
        overlap[j] += 1

m = max(overlap)
print(m)