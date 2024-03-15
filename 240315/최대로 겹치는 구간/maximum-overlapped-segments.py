n = int(input())

line = [] # 선분 담을 tuple
for i in range(n):
    x1, x2 = map(int, input().split())
    x1 += 100
    x2 += 100
    line.append((x1, x2))

overlap = [0]*(201)

for i in line: # 각각의 선분에 대해 iteration
    for j in range(i[0], i[1]): # range(x1, x2)
        overlap[j] += 1

maxx = max(overlap)
print(maxx)