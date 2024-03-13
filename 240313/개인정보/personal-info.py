lst = []

for i in range(5):
    name, h, w = input().split()
    lst.append((name, int(h), float(w)))

print('name')
lst.sort(key=lambda x: x[0])
for elem in lst:
    print(elem[0], elem[1], elem[2])

print()
print('height')
lst.sort(key=lambda x: -x[1])
for elem in lst:
    print(elem[0], elem[1], elem[2])