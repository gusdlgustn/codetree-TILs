n = int(input())

lst = []
for i in range(n):
    name, height, weight = tuple(input().split())
    lst.append((name, height, weight))


lst.sort(key = lambda x: x[1])

for elem in lst:
    print(elem[0], elem[1], elem[2])