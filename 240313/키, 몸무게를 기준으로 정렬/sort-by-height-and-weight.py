n = int(input())

lst = []
for i in range(n):
    name, h, w = input().split()
    lst.append((name, int(h), int(w)))

lst.sort(key=lambda x:(x[1], -x[2]))

for e in lst:
    print(e[0], e[1], e[2])